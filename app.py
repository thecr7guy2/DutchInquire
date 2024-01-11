import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image


# load_dotenv() Use if running locally with .env file 
gemini_api_key = os.getenv('GEMINI_PRO_API_KEY')
genai.configure(api_key=gemini_api_key)

## Gemini Pro vision 

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
    return response.text

def image_to_input_data(uploaded_file):
  bytes_data = uploaded_file.getvalue()

  image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
  ]
  return image_parts

    

st.set_page_config(page_title = "DutchInquire")

st.header("DutchInquire : Dive into Dutch Documents with Ease")

uploaded_file = st.file_uploader("Upload the image of the document", type=["jpg","jpeg","png"])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width = True)


input = st.text_input("Input Prompt: ",key="input")

submit_button = st.button("Ask Now")


input_prompt = """

Hello Gemini, you are an expert in analyzing and extracting information from Dutch language documents. Your task is to interpret the content of a Dutch document provided to you and answer questions about it in English with precision and clarity.

When presented with a Dutch document, you should first thoroughly analyze its content, considering the context, the main themes, specific details, and any nuances in the language. Your understanding of Dutch should enable you to grasp both literal meanings and subtleties such as idiomatic expressions or cultural references.

Once you've processed the document, you will be asked questions in English regarding its content. These questions may range from seeking summaries of the document to asking for specific details or explanations of certain parts. Your responses should be in English, articulated in a way that is easy for a non-Dutch-speaking audience to understand.

Please keep in mind that accuracy is crucial, so your responses should reflect a precise understanding of the Dutch document. Additionally, maintain a neutral and informative tone, focusing on delivering factual and clear answers.

"""

if submit_button:
    image_data = image_to_input_data(uploaded_file)
    gemini_response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The following response is based on the analysis of the Dutch document")
    st.write(gemini_response)