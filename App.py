import streamlit as st
from Pages import Home, One, Two, Three
from streamlit_navigation_bar import st_navbar as navbar

st.set_page_config(initial_sidebar_state="collapsed")
pages = ['Home', 'One', 'Two', 'Three']

styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(105, 114, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    }
}

page = navbar(pages, styles=styles)

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