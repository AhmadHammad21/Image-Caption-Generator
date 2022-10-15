import streamlit as st
from generate_caption import return_caption
from tempfile import NamedTemporaryFile
from tensorflow.keras.preprocessing.image import load_img


# setting the title of our app
st.title("Image Cpation Generator")
caption = ""
# file uploader

buffer = st.file_uploader("Upload your image")
temp_file = NamedTemporaryFile(delete=False)
if buffer:
    temp_file.write(buffer.getvalue())
    img = load_img(temp_file.name)
    caption = return_caption(img)
    st.image(buffer)


# # removing the start and end words, so it looks nicer
caption = caption[5: -4]

# displaying this message
st.text("Caption Generated: ")

# displaying the generated caption
st.text(caption)

# showing the image that was put
