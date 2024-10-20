import requests
import streamlit as st
import json


def get_groq_response(language, input_text):
    json_body = {
                  "input": {
                      "language": language,
                      "text": input_text
                  },
                  "config": {},
                  "kwargs": {}
                }
    
    json_body = json.dumps(json_body, indent=4)
    response = requests.post("http://127.0.0.1:8000/chain/invoke", json_body)

    # print(response.json())
    return response.json()['output']

## Streamlit app
st.title("LLM Application Using LCEL")
language = st.text_input("Enter the Language to which you want to translate your text")
input_text = st.text_input("Enter the text you want to convert to french")

if language and input_text:
    st.write(get_groq_response(language, input_text))