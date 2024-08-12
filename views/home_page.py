import streamlit as st
import base64

# Define a function to load and encode image
def load_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load and display background image
image_base64 = load_image("assets/Shadow3.jpeg")
st.markdown(
    f"""
    <style>
    body {{
        margin: 0; /* Remove default body margin */
        padding: 0; /* Remove default body padding */
    }}
    .home-page {{
        position: relative;
        width: 97vw; /* Full viewport width */
        height: 450px;
        background-image: url('data:image/jpeg;base64,{image_base64}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        border-radius: 20px;
        overflow: hidden;
        margin-left: -60px; /* Negative margin to push left */
        margin-right: 0; /* Remove right margin */
        padding: 0; /* Remove padding */
    }}
    
    
    .content {{
        text-align: center;
        color: white;
        background: rgba(0, 0, 0, 0.6);
        padding: 40px;
        border-radius: 15px;
        margin: 30px auto; /* Adjust margin-top for space between cover and content */
        max-width: 1200px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }}
    </style>
    <div class="home-page">
    </div>
    """,
    unsafe_allow_html=True
)

# Content of the homepage
st.markdown("""
    <div class="content">
        <h2 style="font-size: 2.5rem;">Welcome to My AI Projects Showcase</h2>
        <h3 style="font-size: 2rem;">I’m <span style="color: #6315e7;">Mehran Hamayoon</span></h3>
        <p style="font-size: 1.2rem;">
            This is a collection of my innovative applications of machine learning and artificial intelligence. 
            Below are some of the featured projects I've been working on.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Create columns for the 2x2 grid
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
        <div style="background: rgba(0, 0, 0, 0.7);
                color: white; padding: 20px;
                border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                text-align: center; display: flex;
                flex-direction: column;
                height: 300px;">
                <h2>Featured Projects</h2>
                <ul style="list-style-type: none; padding: 0; margin: 0;">
                <li style="margin: 10px 0;"><strong>Project 1:</strong> Math with AI - <a href="http://localhost:8501/mathwithai" target="_blank" style="color: #6315e7;">View Project</a></li>
                <li style="margin: 10px 0;"><strong>Project 2:</strong> Pong Game - <a href="http://localhost:8501/Pong_Game" target="_blank" style="color: #6315e7;">View Project</a></li>
                <li style="margin: 10px 0;"><strong>Project 3:</strong> Real-Time Background Replacement - <a href="http://localhost:8501/Background_Image_Changer" target="_blank" style="color: #6315e7;">View Project</a></li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background: rgba(0, 0, 0, 0.7);
                 color: white; padding: 20px;
                 border-radius: 10px;
                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                 text-align: center;
                 height: 300px;">
            <h2>Technologies Used</h2>
            <p>
                Streamlit, OpenCV, cvzone, HandTrackingModule, Google Generative AI, NumPy, SelfiSegmentationModule
            </p>
        </div>
    """, unsafe_allow_html=True)

# Add margin between rows
st.markdown("""
    <div style="margin: 20px 0;"></div> <!-- Margin between rows -->
    """,
    unsafe_allow_html=True
)

# Create the second row of columns
col3, col4 = st.columns([1, 1])
with col3:
    st.markdown("""
        <div style="background: rgba(0, 0, 0, 0.7);
                 color: white; padding: 20px;
                 border-radius: 10px;
                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                 text-align: center; height: 300px;">
            <h2>Contact</h2>
            <p>
                You can reach out to me at <a href="mailto: mehranwazir00@gmail.com" style="color: #6315e7;">mehanwazir00@gmail.com</a>.
            <p>
                Follow me on <a href="https://github.com/mehranwazir" target="_blank" style="color: #6315e7;">Github</a> and <a href="https://www.linkedin.com/in/mehran-hamayoon-5b0713299" target="_blank" style="color: #6315e7;">LinkedIn</a>.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div style="background: rgba(0, 0, 0, 0.7);
                 color: white; padding: 20px;
                 border-radius: 10px;
                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                 text-align: center; height: 300px;">
            <h2>About Me</h2>
            <p>
                I’m Mehran Hamayoon, a machine learning enthusiast with a passion for building innovative AI solutions.
            </p>
        </div>
    """, unsafe_allow_html=True)
