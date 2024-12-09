import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

class Home:
    def __init__(self):
        self.lottie = self.load_lottieurl("https://lottie.host/f8debb1e-8147-429f-95fb-7f453b37cd70/Bz4LrFhHTN.json")
        self.toni = Image.open("img/toni.png")

    def load_lottieurl(self, url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()



    def app(self):

        with st.container():
            st.title("Welcome to the Home page")
        with st.container():
            st.write("---")
            lef, righ = st.columns(2)
            with lef:
                st.header("exaaample")
                st.write("This project (streamlit) will analyze any dataset and create a user-friendly table and also "
                         "create graphs with any values from dataset.")
            with righ:
                st_lottie(self.lottie, height=300, key="coding")

        with st.container():
            st.header("Ooooooooo")
            imageg, teext = st.columns((1, 2))
            with imageg:
                st.image(self.toni)
            with teext:
                st.subheader("Simple man")
                st.write(
                    """
                    This video contains useful information about our future life
                    you should watch this!
                    """
                )
                st.markdown("[Watch Video...](https://www.youtube.com/watch?v=frAhxXbLetk)")