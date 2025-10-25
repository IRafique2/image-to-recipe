import os
from dotenv import load_dotenv, find_dotenv
from langchain import PromptTemplate, LLMChain
from transformers import pipeline
from langchain_ollama import OllamaLLM
import requests
import streamlit as st
import io
from PIL import Image  # Import PIL for image handling
from functools import lru_cache

# Initialize and cache Ollama model using LRU Cache (Least Recently Used)
@lru_cache(maxsize=1)  # Cache the model to avoid reloading every time
def initialize_ollama_model():
    model = OllamaLLM(model="gemma3:1b", temperature=0.7)
    return model

# Load environment variables
load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# Implement image-to-text model
def image_to_text(image_bytes):
    # Convert the image bytes to a PIL Image
    image = Image.open(image_bytes)

    # Initialize image-to-text pipeline
    pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    
    # Pass the PIL image to the pipeline
    text = pipe(image)[0]['generated_text']
    return text

# Text-to-speech model
def text_to_speech(text):
    API_URL = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-36"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Generate recipe function
def generate_recipe(ingredients):
    # Define the LangChain template
    template="""
            u are a extremely knowledgeable nutritionist, bodybuilder and chef who also knows everything one needs to know about the best quick, healthy recipes.

         You know all there is to know about healthy foods, healthy recipes that help people lean and build muscles, and lose stubborn fat.
         You've also trained many top-performing athletes in bodybuilding, and in achieving an amazing physique.
         You understand how to help people who don't have much time or ingredients to make meals fast depending on what they can find in their kit.

        Your job is to assist users with questions related to finding the best cooking instructions depending on the following variables:
        - {ingredients}

        When finding the best recipes and instructions to cook, you'll answer with confidence and to the point.

        Keep in mind the time constraint of 5-10 minutes when coming up with recipes and instructions, as well as the recipe.

        If the {ingredients} are less than 3, feel free to add a few more as long as they will complement the healthy meal.

        Make sure to format your answer as follows:

        - **The name of the meal**  
        - **Best for recipe category**  
        - **Preparation Time** (header)  
        - **Difficulty** (bold): Easy  
        - **Ingredients** (bold)  
        - List all ingredients  
        - **Kitchen tools needed** (bold)  
        - List kitchen tools needed  
        - **Instructions** (bold)  
        - List all instructions to put the meal together  
        - **Macros** (bold):  
        - Total calories  
        - List each ingredient's calories  
        - List all macros  

        Please make sure to be brief and to the point.

        Make the instructions easy to follow and step-by-step.

    """
    prompt = PromptTemplate(
        input_variables=["ingredients"],
        template=template
    )
    
    model = initialize_ollama_model()  # Use cached model
    recipe_chain = LLMChain(llm=model, prompt=prompt)
    recipe = recipe_chain.run(ingredients=ingredients)
    return recipe

# Main function to process the uploaded file
def process_image(uploaded_file):
    file_bytes = uploaded_file.getvalue()
    image_url = io.BytesIO(file_bytes)  # Process in memory
    ingredients = image_to_text(image_url)

    # Generate recipe and text-to-speech
    recipe = generate_recipe(ingredients)
    audio = text_to_speech(ingredients)

    return ingredients, recipe, audio

# Run Streamlit app
def main():
    st.title("Recipe Generator App")
    st.header("Generate Quick and Healthy Recipes Based on Your Ingredients")

    uploaded_file = st.file_uploader("Upload an image of your ingredients", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="The uploaded image", use_container_width=True)

        # Process the image
        ingredients, recipe, audio = process_image(uploaded_file)

        # Display ingredients and recipe in expandable sections
        with st.expander("Ingredients"):
            st.write(ingredients)

        with st.expander("Recipe"):
            st.write(recipe)

        # Save audio and play it
        with open('audio.flac', 'wb') as file:
            file.write(audio)

        st.audio('audio.flac')

if __name__ == "__main__":
    main()
