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
        
        page_title="airbnb analysis",
        page_icon="",
        layout = "wide"
    )
df_csv = pd.read_csv("airbnb.csv")
df=pd.DataFrame(df_csv)

def func_all ():
    df_csv = pd.read_csv("airbnb.csv")
    df=pd.DataFrame(df_csv)
    
    #average, sum of reviews
    df_mean = df["number_of_reviews"].mean().sum()
    df_sum =  df["number_of_reviews"].sum()
    st.write("average reviews",round(df_mean, 2))
    st.write("sum of no of reviews",df_sum)
    
    #count host neighbourhood
    list_neighbour = list(set(df["host_neighbourhood"]))
    df_count_neighbour =pd.Series(list_neighbour).value_counts().sum()
    st.write("count of neighbourhood",df_count_neighbour)
    
    #count host id
    list_host_id = list(set(df["host_id"]))
    df_count_host_id =pd.Series(list_host_id).value_counts().sum()
    st.write("count of host id",df_count_host_id)
    
    #room type price
    room_types = df.groupby("room_type")[["price"]].sum()
    room_types.reset_index(inplace=True)
    df_room_types = room_types
    st.dataframe(df_room_types, use_container_width=True) 
    st.bar_chart(df_room_types.set_index('room_type'))
    #df_price_roomtypes = pd.Series(list_neighbour).value_counts()
    
    #average price of neighbourhood
    avg_neighbour = df.groupby("host_neighbourhood")[["price"]].mean() 
    avg_neighbour.reset_index(inplace=True)
    st.dataframe(avg_neighbour.head(10), use_container_width=True) 
    st.bar_chart(avg_neighbour.set_index('host_neighbourhood'))
    # styled_df = avg_neighbour_room_new.style.background_gradient(subset=['price'], cmap='coolwarm')
    
    #total room type price
    tot_neighbour_room = df.groupby(["host_neighbourhood","room_type"])["price"].sum() 
    tot_neighbour_room = tot_neighbour_room.reset_index()
    cols = tot_neighbour_room.columns.tolist()
    cols[0], cols[1] = cols[1], cols[0]  # Swap 'host_neighbourhood' and 'room_type'
    tot_neighbour_room = tot_neighbour_room[cols]
    tot_neighbour_room_new = tot_neighbour_room.pivot(index='host_neighbourhood', columns='room_type', values='price')
    st.dataframe(tot_neighbour_room_new, use_container_width=True)
    
    #top host by total reviews
    review_group = df[['name','country','review_scores','number_of_reviews']]
    review_group = review_group.reset_index(drop=True)
    top_hotel_reviews = review_group.sort_values(by=['review_scores', 'number_of_reviews'], ascending=[False, False])
    top_hotel_reviews = top_hotel_reviews.reset_index(drop=True)
    top_hotel_reviews = top_hotel_reviews.rename(columns={
    'name': 'Hotel Name', 
    'review_scores': 'Review Scores', 
    'number_of_reviews': 'Number of Reviews',
    'country':'Country Name'})
    st.dataframe(top_hotel_reviews.head(10), use_container_width=True)
    st.bar_chart(data=top_hotel_reviews.head(10),x='Hotel Name', y='Number of Reviews',horizontal=True,use_container_width=True)
    
    cancel_policy = df['cancellation_policy'].value_counts().reset_index()
    cancel_policy.columns = ['cancellation_policy', 'count']
    st.dataframe(cancel_policy, use_container_width=True)
    fig1 = px.pie(cancel_policy, values='count', names='cancellation_policy', title='Cancellation Policy')
    st.plotly_chart(fig1)
    
    bedrooms = df['bedrooms'].value_counts().reset_index()
    bedrooms.columns = ['bedrooms', 'count']
    st.dataframe(bedrooms, use_container_width=True)
    fig2 = px.pie(bedrooms, values='count', names='bedrooms', title='Bedrooms types ')
    st.plotly_chart(fig2)

def func_others(value):
    st.write(value)

# streamlit part
st.title(" AIRBNB DATA ANALYSIS ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

with st.sidebar:
    
    select = option_menu("Main menu",["HOME","ANALYSIS"])
    
    
if select == "HOME":
         
st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        img1 = Image.open("images/phonepe3.jpg")
        st.image( img1,use_column_width=True,channels="RGB" )
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")

elif select == "ANALYSIS":
       list_neighbour = list(set(df["host_neighbourhood"]))
        neighbourhood =  st.selectbox( "Select one", ["All"] + list_neighbour)
        if st.button("Submit"):
             if neighbourhood == "All":
                 func_all()
             else:
                 neighbourhood_name = neighbourhood
                 func_others(neighbourhood_name)  
       
