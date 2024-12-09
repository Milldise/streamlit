import streamlit as st
from Pages import Home, One, Two, Three
from streamlit_navigation_bar import st_navbar as navbar
from PIL import Image
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie
import requests

image = Image.open('img/alien.png')
logo_path = "img/american.svg"



st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)
pages = ['Home', 'One', 'Two', 'Three']

styles = {
    "nav": {
        "background-color": "lightgray",
        "display": "flex",
        "justify-content": "center"
    },
    "img": {
        "position": "absolute",
        "left": "200px",
        "top": "1px",
        "width": "300px",
        "height": "45px",
    },
    "span": {
        "display": "inline-block",
        "color": "black",
        "padding": "0.2rem 0.725rem",
        "font-size": "14px"
    },
    "active": {
        "background-color": "mediumpurple",
        "color": "black",
        "font-weight": "normal",
        "padding": "14px"
    }
}

page = navbar(pages, logo_path=logo_path, styles=styles)

if page == 'Home':
    Home.Home().app()
elif page == 'One':
    One.One().app()
elif page == 'Two':
    Two.Two().app()
elif page == 'Three':
    Three.Three().app()
else:
    Home.Home().app()
