import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import streamlit as st
from PIL import Image

# Function to process video frames
def process_frame(frame, detector, ballPos, speedX, speedY, gameOver, score):
    imgBackground = cv2.imread("assets/Background.png")
    imgGameOver = cv2.imread("assets/gameOver.png")
    imgBall = cv2.imread("assets/Ball.png", cv2.IMREAD_UNCHANGED)
    imgBat1 = cv2.imread("assets/bat1.png", cv2.IMREAD_UNCHANGED)
    imgBat2 = cv2.imread("assets/bat2.png", cv2.IMREAD_UNCHANGED)
    
    frame = cv2.flip(frame, 1)
    imgRaw = frame.copy()

    # Find the hand and its landmarks
    hands, frame = detector.findHands(frame, flipType=False)  # with draw

    # Overlaying the background image
    frame = cv2.addWeighted(frame, 0.2, imgBackground, 0.8, 0)

    # Check for hands
    if hands:
        for hand in hands:
            x, y, w, h = hand['bbox']
            h1, w1, _ = imgBat1.shape
            y1 = y - h1 // 2
            y1 = np.clip(y1, 20, 415)

            if hand['type'] == "Left":
                frame = cvzone.overlayPNG(frame, imgBat1, (59, y1))
                if 59 < ballPos[0] < 59 + w1 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] += 30
                    score[0] += 1

            if hand['type'] == "Right":
                frame = cvzone.overlayPNG(frame, imgBat2, (1195, y1))
                if 1195 - 50 < ballPos[0] < 1195 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] -= 30
                    score[1] += 1

    # Game Over
    if ballPos[0] < 40 or ballPos[0] > 1200:
        gameOver = True

    if gameOver:
        frame = imgGameOver
        cv2.putText(frame, str(score[1] + score[0]).zfill(2), (585, 360), cv2.FONT_HERSHEY_COMPLEX,
                    2.5, (200, 0, 200), 5)

    # If game not over move the ball
    else:
        # Move the Ball
        if ballPos[1] >= 500 or ballPos[1] <= 10:
            speedY = -speedY

        ballPos[0] += speedX
        ballPos[1] += speedY

        # Draw the ball
        frame = cvzone.overlayPNG(frame, imgBall, ballPos)

        cv2.putText(frame, str(score[0]), (300, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
        cv2.putText(frame, str(score[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

    frame[580:700, 20:233] = cv2.resize(imgRaw, (213, 120))

    return frame, ballPos, speedX, speedY, gameOver, score

# Streamlit app
st.title("Pong Game")

# Create layout with two columns
col1, col2 = st.columns([3, 1])

with col2:
    #st.title("About This Project")
    st.markdown("""
    ## About This Project
                
    This interactive game uses hand gestures to control paddles and hit the ball, aiming to score points.

    - **Objective:** Use hand gestures to move paddles and hit the ball to score points. Avoid letting the ball pass your paddle!
    - **Technologies Used:**
      - **Computer Vision:** OpenCV and Cvzone for real-time hand tracking and game graphics.
      - **Game Assets:** Background, ball, and paddle images used to create the game environment.
      - **Programming Languages:** Python.
    - **Features:**
      - **Hand Gesture Recognition:** Move paddles with hand gestures.
      - **Real-time Feedback:** Score points and see game status in real-time.
    """)

with col1:
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.8, maxHands=2)

    # Initialize session state variables
    if 'ballPos' not in st.session_state:
        st.session_state.ballPos = [100, 100]
        st.session_state.speedX = 20  # Increased speedX for faster ball movement
        st.session_state.speedY = 20  # Increased speedY for faster ball movement
        st.session_state.gameOver = False
        st.session_state.score = [0, 0]

    # Streamlit reset button
    if st.button("Reset Game"):
        st.session_state.ballPos = [100, 100]
        st.session_state.speedX = 20  # Reset to increased speed
        st.session_state.speedY = 20  # Reset to increased speed
        st.session_state.gameOver = False
        st.session_state.score = [0, 0]

    # Placeholder for the video feed
    stframe = st.empty()
    
    # Process and display video feed
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process frame
        frame, st.session_state.ballPos, st.session_state.speedX, st.session_state.speedY, st.session_state.gameOver, st.session_state.score = process_frame(
            frame, detector, st.session_state.ballPos, st.session_state.speedX, st.session_state.speedY, st.session_state.gameOver, st.session_state.score)

        # Convert frame to RGB for display in Streamlit
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(img_rgb, channels="RGB")

    cap.release()
