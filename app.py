import streamlit as st
import pytesseract
from PIL import Image

# Function to extract text from the uploaded image
def extract_text(image):
    text = pytesseract.image_to_string(image, lang='eng+hin')  # Extract text using Tesseract
    return text

# Streamlit app layout
st.title("OCR with Keyword Search")
st.write("Upload an image and enter a keyword to search within the extracted text.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Input for keyword search
keyword = st.text_input("Enter Keyword")

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Extract text from the image
    extracted_text = extract_text(image)
    
    # Display the extracted text
    st.subheader("Extracted Text")
    st.write(extracted_text)
    
    if keyword:
        # Search for the keyword in the extracted text
        matching_lines = [line for line in extracted_text.splitlines() if keyword.lower() in line.lower()]
        
        # Display matching lines
        st.subheader("Matching Lines")
        if matching_lines:
            for line in matching_lines:
                st.write(line)
        else:
            st.write("No matching lines found.")
