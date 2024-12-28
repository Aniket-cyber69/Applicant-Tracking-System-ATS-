from dotenv import load_dotenv # type: ignore

load_dotenv()

import streamlit as st # type: ignore
import os 
import io
import base64
from PIL import Image # type: ignore
import pdf2image # type: ignore
import google.generativeai as genai # type: ignore

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(prompt, pdf_content, input):
    # Update to the new model
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Construct the content dictionary according to the expected format
    content = {
        "parts": [
            {
                "text": prompt
            },
            {
                "mime_type": pdf_content[0]["mime_type"],
                "data": pdf_content[0]["data"]
            },
            {
                "text": input
            }
        ]
    }

    # Make the API call with the updated model
    response = model.generate_content(content)
    return response.text




def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",  # Correct key name
                "data": base64.b64encode(img_byte_arr).decode()  # Encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


    
# streamlit APP

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description :", key="input")
uploaded_file=st.file_uploader("Upload your Resume(PDF).....", type=["PDF"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1=st.button("Tell me about the Resume")
#submit2=st.button("How can I improve my skill")
submit3=st.button("percentage match")

input_prompt1="""
 You are an experience HR with tech experience in the filed of Data Science, Full Stack Web devolopment, Big Data Engineering, DEVOPS, 
 Data Analyst, your task is to review the provided resume against the job description for these profiles.
  Please share your professional evaluation on weather the cadidate's profile aligns with the role. Highlight the strengths and weaknesses
  of the applicant in relation to the specified job requirements
"""

input_prompt3="""
 You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack Web devolopment, 
 Big Data Engineering, DEVOPS, Data Analyst and deep ATS functionality, 
 your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches the job
 description. First the output should come as percentage and then keyword missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the Resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the Resume")


 


