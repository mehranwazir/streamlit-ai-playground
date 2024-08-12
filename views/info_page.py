import streamlit as st
from PIL import Image
import base64

# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Load the profile image
profile_image_path = 'assets/profile_picture.jpg'  # Update the path to your profile picture
profile_image_base64 = image_to_base64(profile_image_path)

# Page Title
st.title("About Me")

# Display profile image in a circular frame
st.markdown(f"""
<style>
    .profile-img {{
        width: 300px;
        height: 300px;
        border-radius: 50%;
        border: 3px solid #ddd;  /* Add a border if desired */
        object-fit: cover;
        display: block;
        margin: 0 auto;  /* Center the image horizontally */
    }}
    .profile-container {{
        text-align: center;
        margin-bottom: 20px;  /* Space below the profile image */
    }}
    .intro-box {{
        background: rgba(0, 0, 0, 0.7);
        color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
        margin: 20px auto; /* Center the box with some margin */
        max-width: 100%; /* Adjust to full width of the container */
        text-align: center;
    }}
</style>
<div class="profile-container">
    <img class="profile-img" src="data:image/jpeg;base64,{profile_image_base64}" alt="Profile Image"/>
</div>
""", unsafe_allow_html=True)

# Introduction in a styled box
st.markdown("""
<div class="intro-box">
    Hello! I'm <strong>Mehran Hamayoon</strong>, a passionate Computer Science student with a keen interest in <strong>Machine Learning</strong>, <strong>Deep Learning</strong>, and <strong>Computer Vision</strong>. I am dedicated to leveraging technology to create innovative solutions and solve complex problems.
</div>
""", unsafe_allow_html=True)

# Create three columns with equal width
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background: rgba(0, 0, 0, 0.7);
             color: white; padding: 20px;
             border-radius: 10px;
             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
             text-align: left; margin-bottom: 20px; min-height: 200px;">
        <h2>Background</h2>
        <p>My journey in tech began with a deep curiosity about data and algorithms. This led me to study Computer Science, where I learned about different technologies and programming. As I continued my studies, I became really interested in Machine Learning. I began working with tools like TensorFlow and Keras to build and improve complex models. My experiences in both academic and hands-on projects have given me the skills to tackle exciting challenges in AI, and I’m thrilled about the endless opportunities it presents.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: rgba(0, 0, 0, 0.7);
             color: white; padding: 20px;
             border-radius: 10px;
             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
             text-align: left; margin-bottom: 20px; min-height: 200px;">
        <h2>Current Interest</h2>
        <p>Currently, I am working on several projects that integrate real-time image processing with AI technologies. My focus includes developing applications for hand gesture recognition, background replacement, and interactive AI solutions. I am also exploring Generative AI models and their potential to enhance creativity and automation. These projects allow me to push the boundaries of what’s possible with AI and constantly learn and adapt to new advancements in the field.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: rgba(0, 0, 0, 0.7);
             color: white; padding: 20px;
             border-radius: 10px;
             box-shadow: 0 100px 8px rgba(0, 0, 0, 0.5);
             text-align: left; margin-bottom: 20px; min-height: 200px;">
        <h2>Skills</h2>
        <p>  <strong>Programming Languages</strong>: C++, Python, JavaScript<br>
             <strong>Machine Learning & AI</strong>: TensorFlow, Keras, scikit-learn <br>
             <strong>Computer Vision</strong>: OpenCV, cvzone<br>
             <strong>Web Development</strong>: Streamlit, Node.js, Express<br>
             <strong>Image Processing</strong>: PIL, NumPy<br>       
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
---

Thank you for visiting my portfolio! I look forward to connecting with you.
""")
