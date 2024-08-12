import streamlit as st

st.set_page_config(page_title="Multi-Page App", layout="wide")


from PIL import Image




home_page = st.Page(
    page = "views/home_page.py",
    title= "Home",
    icon = ":material/home:",
    default= True
)

project_1_page = st.Page(
    page = "views/mathwithai.py",
    title= "Math With AI",
    icon= ":material/calculate:",
)

project_2_page = st.Page(
    page = "views/Pong_Game.py",
    title= "Pong Game ",
    icon= ":material/sports_esports:"
)

project_3_page = st.Page(
    page= "views/Background_Image_Changer.py",
    title= "Real-Time Background Replacement",
    icon = ":material/image:"
)

info_page = st.Page(
    page= "views/info_page.py",
    title= "About me",
    icon= ":material/account_circle:"
)

# Open an existing image
image = Image.open('assets/white.png')
st.logo(image, icon_image= image)


# Navigation Setup [Without Sections]
pg = st.navigation({

    "": [home_page],
    "Projects": [project_1_page,project_2_page,project_3_page],
    "Info": [info_page]
    },)

# Run Navigation
pg.run()