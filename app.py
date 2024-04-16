import streamlit as st
import speech_recognition as sr
import requests


def send_text_to_server(text):
    url = "http://127.0.0.1:8888/{response.text}"
    data = {'text': text}
    response = requests.post(url, json=data)
    return response.json()
# Function to send text to server URL and get response
def send_text_to_server(text):
    url = "https://srivatsavdamaraju-last-hope.hf.space/ask/{}".format(text)
    response = requests.get(url)
    return response.text

st.title("Voice to Text Converter")

# Record audio
st.write("Click the button below and speak something...")
if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("Recording...")
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)
        st.write("Recording finished!")

    # Convert audio to text
    try:
        text = recognizer.recognize_google(audio_data)
        st.success("Text: {}".format(text))
        
        # Send text to server and get response
        server_response = send_text_to_server(text)
        st.write("Server Response: {}".format(server_response))
    except sr.UnknownValueError:
        st.error("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        st.error("Sorry, Speech Recognition service is unavailable. Error: {}".format(e))
    except Exception as e:
        st.error("An error occurred: {}".format(e))
