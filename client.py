import requests
import streamlit as st

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8001/poem/invoke",
        json={'input': {'topic': input_text}}
    )
    
    print("Response from API:", response.json())  # Debugging print

    return response.json().get('output', 'No output received')

    ## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text1=st.text_input("Write a poem on")



if input_text1:
    st.write(get_ollama_response(input_text1))