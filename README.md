# AI Projects Showcase

Welcome to my AI Projects Showcase! This repository features a collection of innovative applications built using various AI technologies. The projects utilize computer vision, real-time image processing, and machine learning models to create interactive and engaging experiences.

## Table of Contents

- [Overview](#overview)
- [Project List](#project-list)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Overview

This repository includes the following projects:

1. **Math with AI**: An application that uses real-time hand gestures to interact with an AI model for solving math problems.
2. **Pong Game**: A real-time pong game controlled using hand gestures.
3. **Real-Time Background Replacement**: An application that replaces the background in a webcam feed with images.

Each project is developed using Streamlit and incorporates various AI and computer vision techniques.

## Project List

### 1. Math with AI
- **Description**: An interactive app where users draw math problems using hand gestures. The AI model provides solutions in real time.
- **File**: `mathwithai.py`

### 2. Pong Game
- **Description**: A pong game where users control the paddles using hand gestures. The game features real-time updates and a game-over screen.
- **File**: `Pong_Game.py`

### 3. Real-Time Background Replacement
- **Description**: A real-time background changer that allows users to replace the background of their webcam feed with chosen images.
- **File**: `Background_Image_Changer.py`

## Technologies Used

- **Streamlit**: For building interactive web applications.
- **OpenCV**: For real-time image processing and computer vision tasks.
- **cvzone**: For hand tracking and gesture recognition.
- **Google Generative AI**: For generating responses and solving math problems.
- **PIL**: For image processing tasks.

## Installation

To run the projects locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add your Google Generative AI API key:

    ```env
    API_KEY=your_google_generative_ai_api_key
    ```

## Usage

To run a specific project, use Streamlit to start the app:

```bash
streamlit run path/to/your/project.py
