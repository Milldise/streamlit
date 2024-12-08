import streamlit as st
from Pages import Home, One, Two, Three
from streamlit_navigation_bar import st_navbar as navbar
from PIL import Image
import pandas as pd
import numpy as np


image = Image.open('img/alien.png')
logo_path = "img/american.svg"

st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)
pages = ['Home', 'One', 'Two', 'Three']

styles = {
    "nav": {
        "background-color": "royalblue",
        "display": "flex",
        "justify-content": "center"
    },
    "img": {
        "position": "absolute",
        "left": "-20px",
        "font-size": "15px",
        "top": "4px",
        "width": "100px",
        "height": "40px",

    },
    "span": {
        "display": "block",
        "color": "white",
        "padding": "0.2rem 0.725rem",
        "font-size": "14px"
    },
    "active": {
        "background-color": "white",
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
    st.title('hello')