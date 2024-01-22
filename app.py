from pathlib import Path
import requests
from PIL import Image

import streamlit as st
from streamlit_lottie import st_lottie


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "Tilda-Johansson-CV.pdf"
profile_pic = current_dir / "assets" / "pfp.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Tilda Johansson"
PAGE_ICON = "👩‍💼"
NAME = "Tilda Johansson"
title1 = "Backend Developer"
title2 = "Machine Learning Enthusiast"
EMAIL = "tildajson00@gmail.com"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & ASSETS ---


def css_file(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


css_file("styles/styles.css")

profile_pic = Image.open(profile_pic)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_books = load_lottieurl(
    "https://lottie.host/347f3fae-c245-4913-9171-1f447b038fde/7F6iKTArqg.json")

lottie_chat = load_lottieurl(
    "https://lottie.host/28ef266a-47fc-432c-bf0f-ecf6e08fa161/ykjy0Db4Xq.json")

lottie_db = load_lottieurl(
    "https://lottie.host/768e0dce-e55a-4101-b6f7-56e8781764b8/V2MUPgwfT5.json")

lottie_bot = load_lottieurl(
    "https://lottie.host/f3e1a6c4-3780-4de9-acda-4c28762a9d7a/cREuyfm2bd.json")


# --- PROFILE SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(f"**{NAME}**")
    st.write(
        f"**{title1}** and **{title2}** from the north of Sweden, embracing challenges with a passion for constant growth.")
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("🔗", "[Github Profile](https://github.com/tildajson)")


# --- SKILLS ---
st.write("##")
st.write('\n')
st.subheader("Technical Skills")

st.write(
    """
- 👩‍💻 Programming: Python, JavaScript, Linux, Git, Machine Learning, Computer Vision, OOP, TDD
- 💻 Backend Development: Django, Flask, Docker, Node.JS, Express, REST API
- 🎨 Frontend Development: React, HTML/CSS, Bootstrap
- 📚 Databases: Postgres, MongoDB, MySQL, SQLite
- 🔧 Tools: AWS, Jupyter Notebook, Visual Studio, PyTorch, Streamlit
"""
)

st.write("##")

# --- PROJECTS ---
with st.container():
    st.subheader("Featured Projects")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_bot, height=300, key="bot")
    with text_column:
        st.subheader(
            "PasswordVault - Cyber Security Toolkit with Machine Learning Elements")
        st.write(
            """
            Deployed Streamlit / Python web app.\n
            This project consists of a powerful collection of tools intended
            to assist users with enhancing their online safety and privacy.
            Easy to use and navigate so anyone can benefit from the tools provided, despite
            previous technical experience.\n
            Two factor authentication and password manager in progress.
            """
        )
        link1, link2 = st.columns((1, 2))
        with link1:
            st.markdown(
                "[Live Demo](https://passwordvault.streamlit.app/)")
        with link2:
            st.markdown(
                "[Source Code](https://github.com/tildajson/PasswordVault)")


st.write("##")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_books, height=300, key="books")
    with text_column:
        st.subheader("BookBuddy - Reading Tracker Web App for all book lovers")
        st.write(
            """
            Scalable full stack Django web app featuring authentication, authorization and GUI.\n
            As an avid reader myself, I understand the struggle of keeping track of all your books.
            This project strives to improve the reading experience for users by providing an accessible and
            efficient way to track your reading progress.\n
            Book recommendation section and CRUD feature in progress.
            """
        )
        link1, link2 = st.columns((1, 2))
        with link1:
            st.markdown(
                "[Video Demo](https://youtu.be/TFzdeR5T1sE)")
        with link2:
            st.markdown(
                "[Source Code](https://github.com/tildajson/BookBuddy)")


st.write("##")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_chat, height=300, key="chat")
    with text_column:
        st.subheader(
            "Social Sphere - Online Chat App to connect with anyone, anywhere")
        st.write(
            """
            Full stack Flask web app.\n
            Real time chat app built with Flask, Socket.IO and Bootstrap. This project
            allows users to create new chat rooms, or connect to already existing ones
            with a unique room ID.
            """
        )
        st.markdown(
            "[Source Code](https://github.com/tildajson/SocialSphere)")

st.write("##")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_db, height=300, key="db")
    with text_column:
        st.subheader("Recipe REST API - Simplify your cooking experience")
        st.write(
            """
            Backend REST API built with Django and Docker.\n
            This project allows users to create and find recipes in the database. Includes
            authentication, authorization, CRUD, filtering objects and uploading images.\n
            React frontend code in progress.
            """
        )
        st.markdown(
            "[Source Code](https://github.com/tildajson/recipe-REST-API)")
