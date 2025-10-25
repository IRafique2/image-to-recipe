---

# **Recipe Generator App**

The **Recipe Generator App** is a Streamlit-based web application that allows users to generate quick and healthy recipes based on the ingredients they have. Users can upload an image of their ingredients, and the app uses **image-to-text** and **text-to-speech** technologies to provide a recipe and audio instructions. This app is ideal for individuals looking to make nutritious meals with limited ingredients and time.

## **Features**

* **Image-to-Text**: Convert an image of ingredients into text using an image captioning model.
* **Recipe Generation**: Generate quick, healthy recipes based on the ingredients extracted from the image.
* **Text-to-Speech**: Convert the recipe text into speech so users can listen to instructions hands-free.
* **Streamlit Interface**: A simple, interactive interface to upload images, view generated recipes, and listen to audio instructions.

## **Technologies Used**

* **Streamlit**: Framework to build the user interface.
* **Transformers (HuggingFace)**: For image captioning (Salesforce/blip-image-captioning-base) and text-to-speech (facebook/fastspeech2-en-36).
* **LangChain**: For integrating language models (Ollama) with prompts and chains to generate the recipe.
* **PIL (Python Imaging Library)**: For handling and processing images.
* **Requests**: For interacting with APIs.
* **Python-dotenv**: For loading environment variables (e.g., HuggingFace API Token).

## **How It Works**

1. **Upload Ingredients Image**: Users can upload an image containing their ingredients.
2. **Image-to-Text Conversion**: The app uses the **BLIP** image captioning model to extract text (ingredients) from the uploaded image.
3. **Generate Recipe**: The extracted ingredients are passed to a language model (via **LangChain**) to generate a recipe tailored to the ingredients, keeping in mind the time constraint (5-10 minutes).
4. **Text-to-Speech**: The recipe is then converted into speech using the **FastSpeech2** model for hands-free listening.
5. **Display Results**: The app displays the ingredients, recipe, and provides an audio player to listen to the recipe instructions.

## **Setup Instructions**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/recipe-generator-app.git
   cd recipe-generator-app
   ```

2. **Set Up Environment Variables:**

   Create a `.env` file in the project root directory and add your HuggingFace API token:

   ```bash
   HUGGINGFACE_API_TOKEN=your-huggingface-api-token
   ```

3. **Run the Streamlit App:**

   After installing the dependencies and setting up environment variables, run the app:

   ```bash
   streamlit run app.py
   ```

   The app will be accessible at `http://localhost:8501`.

## **File Structure**

```
.
├── app.py                # Main Streamlit application
├── helper.py             # Helper functions for image processing, recipe generation, etc.
├── .env                  # Environment variables (HuggingFace API Token)
└── README.md             # This README file
```

## **Dependencies**

The required dependencies are listed in the `requirements.txt` file:

```txt
streamlit
langchain
requests
transformers
python-dotenv
Pillow
```

## **Environment Variables**

This project requires the following environment variable:

* **HUGGINGFACE_API_TOKEN**: Your HuggingFace API token for accessing the text-to-speech model.

## **How to Use the App**

1. Open the app in your browser (it will run at `http://localhost:8501`).
2. Upload an image of your ingredients.
3. The app will process the image, generate a recipe, and provide the option to listen to the recipe instructions.
4. You can expand the sections to view the ingredients and recipe in text form.

## **Contributing**

To contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make changes or add features.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature-name`).
6. Create a pull request to merge your changes.



Let me know if you'd like to modify any part of this README or if you need additional information!
