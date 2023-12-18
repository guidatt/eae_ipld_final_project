# The library you have to use
import numpy as np

# Some extra libraries to build the webapp and deal with images and files
import streamlit as st
import io
from PIL import Image


# ----- Page configs -----
st.set_page_config(
    page_title="<Your Name> Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.write("Interactive Project to open, crop, display and save images using NumPy, PIL and Matplotlib.")


# ----- Title of the page -----
st.title("🖼️ Image Cropper")
st.divider()


# ----- Getting the image from the user or using a default one if the user didn't upload any, we get the image as a numpy array called img_arr -----
is_example = False
img = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])

if img is None:
    is_example = True
    with Image.open("data/starry_night.png") as img:
        img_arr = np.array(img)
else:
    with Image.open(img) as img:
        img_arr = np.array(img)

# Displaying the image
st.image(img_arr, caption="Original Image" if not is_example else "Original example image", use_column_width=True)
st.write("#")


# TODO: Ex. 1.1: Get the minimum and maximum values for the vertical and horizontal ranges, so the size of the img_arr array -----

def get_max(img):
    with Image.open(img) as img:
        width, height = img.size
        return width, height
    
max_height = get_max(img)
max_width = get_max(img)

print(f"Height: {max_height} pixels")
print(f"Width: {max_width} pixels")


# ----- Creating the sliders to receive the user input with the dimensions to crop the image ----- 
if type(max_height) == int and type(max_width) == int:
    
    cols1 = st.columns([4, 1, 4])

    # this returns a tuple like (100, 300), for the veritcal range to crop
    crop_min_h, crop_max_h = cols1[0].slider("Crop Vertical Range", max_height, max_height, (int(max_height*0.1), int(max_height*0.9)))   
    # this returns a tuple like (100, 300), for the horizontal range to crop
    crop_min_w, crop_max_w = cols1[2].slider("Crop Horizontal Range", max_width, max_width, (int(max_width*0.1), int(max_width*0.9)))    


    st.write("## Cropped Image")

else:
    st.subheader("⚠️ You still need to develop the Ex 1.1.")


# TODO: Ex. 1.3: Crop the image array img_arr using the crop_min_h, crop_max_h, crop_min_w and crop_max_w values -----

crop_min_h = 300
crop_max_h = 600
crop_min_w = 550
crop_max_w = 800

img_shape = (1089, 1377, 4)
img = np.random.random(img_shape)

crop_arr = img[crop_min_h:crop_max_h, crop_min_w:crop_max_w, :]

print(f"Shape: {crop_arr.shape}")

# ----- Displaying the cropped image and creating a download button to download the image -----

if type(crop_arr) == np.ndarray:
    st.image(crop_arr, caption="Cropped Image", use_column_width=True)

    buf = io.BytesIO()
    Image.fromarray(crop_arr).save(buf, format="PNG")
    cropped_img_bytes = buf.getvalue()

    cols2 = st.columns([4, 1, 4])
    file_name = cols2[0].text_input("Chose a File Name:", "cropped_image") + ".png"

    st.download_button(f"Download the image `{file_name}`", cropped_img_bytes, file_name=file_name)

else:
    st.subheader("⚠️ You still need to develop the Ex 1.3.")
