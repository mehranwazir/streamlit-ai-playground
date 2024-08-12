# import streamlit as st
# import cvzone
# import cv2
# from cvzone.HandTrackingModule import HandDetector
# import numpy as np
# import google.generativeai as genai
# import os
# from PIL import Image
# from dotenv import load_dotenv
# # Load environment variables from .env file
# load_dotenv()


# #def math_with_ai_page():
# st.title("Math with AI")

# # Sidebar controls
# col1, col2 = st.columns([2, 1])
# with col1:
#     run = st.checkbox('Run', value=True)
#     FRAME_WINDOW = st.image([])

# with col2:
#     st.title("Answer")
#     output_text_area = st.subheader("No answer yet")

# api_key = os.environ.get('API_KEY')
# genai.configure(api_key=api_key)
# model = genai.GenerativeModel('gemini-1.5-flash')

# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     st.error("Error: Camera not found or unable to open.")
#     st.stop()

# cap.set(propId=3, value=800)
# cap.set(propId=4, value=600)

# detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

# def getHandInfo(img):
#     hands, img = detector.findHands(img, draw=False, flipType=True)
#     if hands:
#         hand = hands[0]
#         lmList = hand["lmList"]
#         fingers = detector.fingersUp(hand)
#         return fingers, lmList
#     else:
#         return None

# def draw(info, prev_pos, canvas):
#     fingers, lmList = info
#     current_pos = None

#     if fingers == [0, 1, 0, 0, 0]:
#         current_pos = lmList[8][0:2]
#         if prev_pos is None:
#             prev_pos = current_pos
#         cv2.line(canvas, current_pos, prev_pos, color=(255, 0, 255), thickness=5)
#     elif fingers == [1, 1, 1, 1, 1]:
#         canvas = np.zeros_like(img)

#     return current_pos, canvas

# def sendToAI(model, canvas, fingers):
#     if fingers == [1, 1, 1, 1, 0]:
#         pil_image = Image.fromarray(canvas)
#         response = model.generate_content(["Solve This Math Problem", pil_image])
#         return response.text


# def format_paragraph(text, words_per_line):
#     words = text.split('\n')
#     lines = []
    
#     # Generate lines with the specified number of words per line
#     for i in range(0, len(words), words_per_line):
#         line = ' '.join(words[i:i + words_per_line])
#         lines.append(line)
    
#     # Join all lines into a single string with newline characters
#     formatted_text = '\n'.join(lines)
#     return formatted_text


# prev_pos = None
# canvas = None
# output_text = ""

# while True:
#     success, img = cap.read()
#     if not success or img is None:
#         st.error("Error: Unable to capture image from camera.")
#         st.stop()
#     img = cv2.flip(img, flipCode=1)
#     if canvas is None:
#         canvas = np.zeros_like(img)

#     info = getHandInfo(img)
#     if info:
#         fingers, lmList = info
#         prev_pos, canvas = draw(info, prev_pos, canvas)
#         output_text = sendToAI(model, canvas, fingers)
#         if output_text:
#             output_text = format_paragraph(output_text,5)

#     image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, gamma=0)
#     FRAME_WINDOW.image(image_combined, channels="BGR")

#     if output_text:
#         output_text_area.text(output_text)

#     cv2.waitKey(1)

# cv2.destroyAllWindows()
# cap.release()

# import streamlit as st
# import cvzone
# import cv2
# from cvzone.HandTrackingModule import HandDetector
# import numpy as np
# import google.generativeai as genai
# import os
# from PIL import Image
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Page Title
# st.title("Math with AI")

# # Sidebar controls
# col1, col2 = st.columns([2, 1])
# with col1:
#     run = st.checkbox('Run', value=True)
#     FRAME_WINDOW = st.image([])

# with col2:
#     st.title("Answer")
#     # Using st.markdown to enable custom CSS for text wrapping
#     output_text_area = st.empty()

# api_key = os.environ.get('API_KEY')
# genai.configure(api_key=api_key)
# model = genai.GenerativeModel('gemini-1.5-flash')

# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     st.error("Error: Camera not found or unable to open.")
#     st.stop()

# cap.set(propId=3, value=800)
# cap.set(propId=4, value=600)

# detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

# def getHandInfo(img):
#     hands, img = detector.findHands(img, draw=False, flipType=True)
#     if hands:
#         hand = hands[0]
#         lmList = hand["lmList"]
#         fingers = detector.fingersUp(hand)
#         return fingers, lmList
#     else:
#         return None

# def draw(info, prev_pos, canvas):
#     fingers, lmList = info
#     current_pos = None

#     if fingers == [0, 1, 0, 0, 0]:
#         current_pos = lmList[8][0:2]
#         if prev_pos is None:
#             prev_pos = current_pos
#         cv2.line(canvas, current_pos, prev_pos, color=(255, 0, 255), thickness=5)
#     elif fingers == [1, 1, 1, 1, 1]:
#         canvas = np.zeros_like(img)

#     return current_pos, canvas

# def sendToAI(model, canvas, fingers):
#     if fingers == [1, 1, 1, 1, 0]:
#         pil_image = Image.fromarray(canvas)
#         response = model.generate_content(["Solve This Math Problem", pil_image])
#         return response.text

# def format_paragraph(text, words_per_line):
#     words = text.split('\n')
#     lines = []
    
#     # Generate lines with the specified number of words per line
#     for i in range(0, len(words), words_per_line):
#         line = ' '.join(words[i:i + words_per_line])
#         lines.append(line)
    
#     # Join all lines into a single string with newline characters
#     formatted_text = '\n'.join(lines)
#     return formatted_text

# prev_pos = None
# canvas = None
# output_text = ""

# while True:
#     success, img = cap.read()
#     if not success or img is None:
#         st.error("Error: Unable to capture image from camera.")
#         st.stop()
#     img = cv2.flip(img, flipCode=1)
#     if canvas is None:
#         canvas = np.zeros_like(img)

#     info = getHandInfo(img)
#     if info:
#         fingers, lmList = info
#         prev_pos, canvas = draw(info, prev_pos, canvas)
#         output_text = sendToAI(model, canvas, fingers)
#         #if output_text:
#          #   output_text = format_paragraph(output_text, 5)

#     image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, gamma=0)
#     FRAME_WINDOW.image(image_combined, channels="BGR")

#     # Use st.markdown for custom CSS styling
#     if output_text:
#         output_text_area.markdown(f"""
#         <div style="max-width: 500px; word-wrap: break-word; white-space: pre-wrap;">
#             {output_text}
#         </div>
#         """, unsafe_allow_html=True)

#     cv2.waitKey(1)

# cv2.destroyAllWindows()
# cap.release()


import streamlit as st
import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
import os
from PIL import Image
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page Title
st.title("Math with AI")

# Sidebar controls
col1, col2 = st.columns([2, 1])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("Answer")
    output_text_area = st.empty()

api_key = os.environ.get('API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    st.error("Error: Camera not found or unable to open.")
    st.stop()

cap.set(propId=3, value=800)
cap.set(propId=4, value=600)

detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        return fingers, lmList
    else:
        return None

def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None

    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, current_pos, prev_pos, color=(255, 0, 255), thickness=5)
    elif fingers == [1, 1, 1, 1, 1]:
        canvas = np.zeros_like(img)

    return current_pos, canvas

def sendToAI(model, canvas, fingers):
    if fingers == [1, 1, 1, 1, 0]:
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["Solve This Math Problem", pil_image])
        return response.text

prev_pos = None
canvas = None
output_text = ""

# Create a placeholder for project information
info_placeholder = st.empty()

# Display project information
info_placeholder.markdown("""
## About This Project

Welcome to the "Math with AI" project! This application leverages real-time hand gesture recognition to interact with an AI model that solves math problems. Here's a brief overview:

- **Objective:** To create an interactive application that uses hand gestures to input mathematical problems, which are then solved by an AI model.
- **Technologies Used:**
  - **Computer Vision:** OpenCV and CVZone for real-time hand tracking.
  - **Machine Learning:** Google Gemini's Generative Model for solving math problems.
  - **Programming Languages:** Python.
- **Features:**
  - **Hand Gesture Recognition:** Use hand gestures to draw mathematical problems.
  - **Real-time Feedback:** Get immediate solutions from the AI model.
  - **Interactive UI:** Easy-to-use interface with real-time video feed and answer display.
- **How to use:**
  - **Use Your Index Finger:** Point your index finger straight and move it around in the camera view to draw on the screen
  - **Use an Open Hand:** Spread all five fingers wide and hold your hand in front of the camera. This gesture will clear the screen.
  - **Sending the Math Problem:** Raise your thumb, index finger, middle finger, and ring finger, while keeping your pinky finger down. This gesture will send the drawn math problem to the AI model
                

""")

# Run the loop only if the checkbox is selected
if run:
    while True:
        success, img = cap.read()
        if not success or img is None:
            st.error("Error: Unable to capture image from camera.")
            st.stop()
        img = cv2.flip(img, flipCode=1)
        if canvas is None:
            canvas = np.zeros_like(img)

        info = getHandInfo(img)
        if info:
            fingers, lmList = info
            prev_pos, canvas = draw(info, prev_pos, canvas)
            output_text = sendToAI(model, canvas, fingers)

        image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, gamma=0)
        FRAME_WINDOW.image(image_combined, channels="BGR")

        if output_text:
            output_text_area.markdown(f"""
            <div style="max-width: 500px; word-wrap: break-word; white-space: pre-wrap;">
                {output_text}
            </div>
            """, unsafe_allow_html=True)

        cv2.waitKey(1)

    cv2.destroyAllWindows()
    cap.release()
