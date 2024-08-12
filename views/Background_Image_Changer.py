# import cv2
# import cvzone
# from cvzone.FPS import FPS
# from cvzone.SelfiSegmentationModule import SelfiSegmentation
# import os
# import streamlit as st
# import numpy as np

# # Function to load and resize images
# def load_images(image_folder, target_size):
#     image_files = os.listdir(image_folder)
#     images = []
#     image_paths = []
#     for image_file in image_files:
#         img = cv2.imread(os.path.join(image_folder, image_file))
#         if img is not None:
#             img_resized = cv2.resize(img, target_size)
#             images.append(img_resized)
#             image_paths.append(image_file)  # Store the file name for reference
#     return images, image_paths

# # Streamlit layout
# st.title('Real-Time Background Replacement')

# # Initialize video capture
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)  # Width
# cap.set(4, 480)  # Height
# cap.set(cv2.CAP_PROP_FPS, 60)

# # Initialize segmentation and FPS objects
# segmentor = SelfiSegmentation()
# fpsReader = FPS()

# # Load images and resize them to the frame size
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
# imgList, image_paths = load_images("Images", (frame_width, frame_height))

# # Initialize state for image index
# if 'IndexImg' not in st.session_state:
#     st.session_state.IndexImg = 0

# def update_index(index):
#     st.session_state.IndexImg = index

# # Create a placeholder for the camera feed
# frame_window = st.empty()

# # Display available backgrounds for selection
# st.subheader("Select a Background")
# col1, col2, col3 = st.columns(3)
# for i, path in enumerate(image_paths):
#     image = imgList[i]
#     # Display image thumbnail
#     with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
#         if st.button(f"Select {path}", key=f"button_{i}"):
#             update_index(i)
#         st.image(image, caption=path, width=100)  # Display thumbnail

# # Create buttons below the camera feed
# st.write("Press the button to change the background:")
# col1, col2 = st.columns([1, 1])
# with col1:
#     if st.button('Previous'):
#         if st.session_state.IndexImg > 0:
#             update_index(st.session_state.IndexImg - 1)
# with col2:
#     if st.button('Next'):
#         if st.session_state.IndexImg < len(imgList) - 1:
#             update_index(st.session_state.IndexImg + 1)

# while True:
#     success, img = cap.read()
#     if not success:
#         break

#     # Get the current background image
#     imgBg = imgList[st.session_state.IndexImg]

#     imgOut = segmentor.removeBG(img, imgBg, cutThreshold=0.45)

#     imgStacked = cvzone.stackImages([img, imgOut], 2, 1)

#     # Update FPS
#     _, imgStacked = fpsReader.update(imgStacked)  # Update FPS with the stacked image

#     # Convert image to RGB for Streamlit
#     imgRGB = cv2.cvtColor(imgStacked, cv2.COLOR_BGR2RGB)

#     # Resize image for display if needed
#     display_width = 960  # Desired width for display
#     display_height = int((display_width / imgRGB.shape[1]) * imgRGB.shape[0])
#     imgRGB_resized = cv2.resize(imgRGB, (display_width, display_height))

#     # Display the image in Streamlit
#     frame_window.image(imgRGB_resized)

# # Release resources
# cv2.destroyAllWindows()
# cap.release()


import cv2
import cvzone
from cvzone.FPS import FPS
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import streamlit as st
import numpy as np

# Function to load and resize images
def load_images(image_folder, target_size):
    image_files = os.listdir(image_folder)
    images = []
    image_paths = []
    for image_file in image_files:
        img = cv2.imread(os.path.join(image_folder, image_file))
        if img is not None:
            img_resized = cv2.resize(img, target_size)
            images.append(img_resized)
            image_paths.append(image_file)  # Store the file name for reference
    return images, image_paths

# Streamlit layout
st.title('Real-Time Background Replacement')

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height
cap.set(cv2.CAP_PROP_FPS, 60)

# Initialize segmentation and FPS objects
segmentor = SelfiSegmentation()
fpsReader = FPS()

# Load images and resize them to the frame size
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
imgList, image_paths = load_images("Images", (frame_width, frame_height))

# Initialize state for image index
if 'IndexImg' not in st.session_state:
    st.session_state.IndexImg = 0

def update_index(index):
    st.session_state.IndexImg = index

# Create a placeholder for the camera feed
frame_window = st.empty()

# Display available backgrounds for selection
st.subheader("Select a Background")
col1, col2, col3 = st.columns(3)
for i, path in enumerate(image_paths):
    image = imgList[i]
    # Display image thumbnail
    with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
        if st.button(f"Select {path}", key=f"button_{i}"):
            update_index(i)
        st.image(image, caption=path, width=100)  # Display thumbnail

# Create buttons below the camera feed
st.write("Press the button to change the background:")
col1, col2 = st.columns([1, 1])
with col1:
    if st.button('Previous'):
        if st.session_state.IndexImg > 0:
            update_index(st.session_state.IndexImg - 1)
with col2:
    if st.button('Next'):
        if st.session_state.IndexImg < len(imgList) - 1:
            update_index(st.session_state.IndexImg + 1)


# Create a placeholder for project information
info_placeholder = st.empty()

# Project information
info_placeholder.markdown("""
## About This Project

Welcome to the "Real-Time Background Replacement" project! This application allows you to replace the background of your webcam feed in real-time using handpicked images. Here’s a brief overview:

- **Objective:** To create an interactive application that enables users to change their webcam background in real-time with various preloaded images.
- **Technologies Used:**
  - **Computer Vision:** OpenCV and CVZone for real-time background segmentation.
  - **Image Processing:** SelfiSegmentation for background removal and replacement.
  - **Programming Languages:** Python.
- **Features:**
  - **Background Replacement:** Swap out the background of your webcam feed with images of your choice.
  - **Real-time Processing:** Immediate application of background changes.
  - **Interactive UI:** Easy-to-use interface with background selection and preview options.

Enjoy experimenting with different backgrounds and see how your webcam feed transforms!
""")

while True:
    success, img = cap.read()
    if not success:
        break

    # Get the current background image
    imgBg = imgList[st.session_state.IndexImg]

    imgOut = segmentor.removeBG(img, imgBg, cutThreshold=0.45)

    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)

    # Update FPS
    _, imgStacked = fpsReader.update(imgStacked)  # Update FPS with the stacked image

    # Convert image to RGB for Streamlit
    imgRGB = cv2.cvtColor(imgStacked, cv2.COLOR_BGR2RGB)

    # Resize image for display if needed
    display_width = 960  # Desired width for display
    display_height = int((display_width / imgRGB.shape[1]) * imgRGB.shape[0])
    imgRGB_resized = cv2.resize(imgRGB, (display_width, display_height))

    # Display the image in Streamlit
    frame_window.image(imgRGB_resized)

# Release resources
cv2.destroyAllWindows()
cap.release()

