import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import numpy as np
import requests
import json

st.set_page_config(
        
        page_title="phoenpe analysis ",
        page_icon="",
        layout = "wide"
    )


st.title("PHONPE DATA VISUALIZATION AND EXPLORATION")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

with st.sidebar:
    
    select = option_menu("Main menu",["HOME","DATA EXPLORATION"])
    
    
if select == "HOME":
         
st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        img1 = Image.open("images/phonepe3.jpg")
        st.image( img1,use_column_width=True,channels="RGB" )
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")

elif select == "DATA EXPLORATION":

        # READ CSV DATA FILE
        df_csv = pd.read_csv("airbnbdata/airbnb.csv")
        df1_copy=pd.DataFrame(df_csv)

