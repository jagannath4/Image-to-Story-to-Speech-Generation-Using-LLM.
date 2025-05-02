---
title: Image Inspired Story Generator
emoji: 📊
colorFrom: indigo
colorTo: pink
sdk: streamlit
sdk_version: 1.42.2
app_file: app.py
pinned: false
short_description: Gemini will generate a plot inspired by the image.
---

# 🖼️📖🔊 Image to Story to Speech Generator using LLM

This application takes an image as input, generates a creative story from it using a large language model (LLM), and then converts the story to natural-sounding speech using a Text-to-Speech (TTS) engine.

Built with **Python**, **Streamlit**, and **transformers-based models**.

---

## 🚀 Features

- 🖼️ **Image Analysis** – Extracts content and meaning from the input image.
- 📖 **Story Generation** – Converts visual content into a coherent narrative using an LLM.
- 🔊 **Speech Synthesis** – Narrates the story using a TTS engine.
- 🌐 **Web UI** – Simple, interactive interface powered by Streamlit.

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jagannath4/Image-to-Story-to-Speech-Generation-Using-LLM
   cd image-story-speech-llm


   Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Install the dependencies


pip install -r requirements.txt

Requirements
Here’s an example of what your requirements.txt might include:
streamlit
torch
transformers
Pillow
gtts  # or pyttsx3 / any other TTS library

▶️ Run the App
streamlit run app.py
