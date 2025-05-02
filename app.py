import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
import base64
from dotenv import load_dotenv
from gtts import gTTS
import io

# Load environment variables from .env file
load_dotenv()

MODEL_ID = "gemini-1.5-flash"
api_key = "AIzaSyB61URBXFORC1D_XFGbYJaPQuQAYk8SrYc"  # Temporarily set directly

# Debug: Print API key (only first few characters for security)
st.write(f"API Key loaded: {api_key[:5]}...")

if not api_key:
    st.error("GEMINI_API_KEY not found in environment variables!")
    st.stop()

genai.configure(api_key=api_key)
enable_stream = False  # Disable streaming for cleaner output

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "model" not in st.session_state:
    st.session_state.model = genai.GenerativeModel(MODEL_ID)
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.model.start_chat()
if "is_new_file" not in st.session_state:
    st.session_state["is_new_file"] = True # Corrected line

# Function to reset chat history
def reset_chat():
    st.session_state.messages = []
    st.session_state.model.start_chat()

def main():
    # Streamlit app
    st.title("Image-Inspired Story Generator")

    # File uploader with allowed types
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Genre selection
    genre = st.selectbox("Select a Genre:", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Thriller", "Horror", "Adventure"])

    if uploaded_file is not None:
        # Determine file type
        file_type = uploaded_file.type
        if file_type.startswith('image'):
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image.", use_container_width=True)
            mime_type = "image/jpeg"  # Use a consistent MIME type for images
        else:
            st.error("Unsupported file type. Please upload an image.")
            st.stop()

        # Reset chat history when a new file is uploaded
        reset_chat()
        st.session_state.is_new_file = True

    # Send button
    if st.button("Generate Story Plot"):
        if not uploaded_file:
            st.warning("Please upload an image.")
            st.stop()

        with st.spinner("Generating story plot..."):
            # Prepare image data for Gemini
            image_bytes = uploaded_file.getvalue()
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            # Prepare the prompt
            prompt = f"Generate a {genre} story plot based on this image."

            # Send file and prompt to Gemini API
            chat = st.session_state.chat
            response = chat.send_message(
                [
                    prompt,
                    {"mime_type": mime_type, "data": base64.b64decode(image_base64)},
                ],
                stream=enable_stream
            )
            st.session_state.is_new_file = False

            # Display Gemini response
            full_response = response.text  # Get the full response
            with st.chat_message("assistant"):
                st.markdown(full_response)  # Display the response as is

            # Add Gemini response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

            # Convert text to speech
            tts = gTTS(text=full_response, lang='en', slow=False)
            audio_bytes = io.BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            
            # Display audio player
            st.audio(audio_bytes, format='audio/mp3')

        st.subheader("Chat History")
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

if __name__ == "__main__":
    main()