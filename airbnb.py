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



df_csv = pd.read_csv("airbnbdata/airbnb.csv")
df=pd.DataFrame(df_csv)

def func_all ():
    df_csv = pd.read_csv("airbnbdata/airbnb.csv")
    df=pd.DataFrame(df_csv)

        
    #average, sum of reviews
    df_mean = df["number_of_reviews"].mean().sum()
    df_sum =  df["number_of_reviews"].sum()
    col1,col2 = st.columns(2)
    with col1: 
      st.subheader("Average Reviews")         
    with col2:  
      st.subheader("Total Reviews")      
    
    col1.metric("",round(df_mean, 2))
    col2.metric("",df_sum)
        
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")  
        
    #count host neighbourhood
    list_neighbour = list(set(df["host_neighbourhood"]))
    df_count_neighbour =pd.Series(list_neighbour).value_counts().sum()
    #st.write("count of neighbourhood",df_count_neighbour)
    #count host id
    list_host_id = list(set(df["host_id"]))
    df_count_host_id =pd.Series(list_host_id).value_counts().sum()
    col3,col4 = st.columns(2)
    with col3: 
      st.subheader("Host Neighbourhood Count")          
    with col4:  
      st.subheader("Host ID Count")      
      
    col3.metric("",df_count_neighbour)
    col4.metric("",df_count_host_id)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ") 
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ") 
        
    #room type price
    room_types = df.groupby("room_type")[["price"]].sum()
    room_types.reset_index(inplace=True)
    df_room_types = room_types   
    
    #total room type price
    st.subheader("Total Price of Room Types")    
    tot_neighbour_room = df.groupby(["host_neighbourhood","room_type"])["price"].sum() 
    tot_neighbour_room = tot_neighbour_room.reset_index()
    cols = tot_neighbour_room.columns.tolist()
    cols[0], cols[1] = cols[1], cols[0]  # Swap 'host_neighbourhood' and 'room_type'
    tot_neighbour_room = tot_neighbour_room[cols]
    tot_neighbour_room_new = tot_neighbour_room.pivot(index='host_neighbourhood', columns='room_type', values='price')
    st.dataframe(tot_neighbour_room_new, use_container_width=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")    
    st.bar_chart(df_room_types.set_index('room_type'))
        
    #average price of neighbourhood
    st.subheader("Average Price of Host Neighbourhood")    
    avg_neighbour = df.groupby("host_neighbourhood")[["price"]].mean() 
    avg_neighbour.reset_index(inplace=True)
    st.dataframe(avg_neighbour.head(10), use_container_width=True) 
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")     
    st.bar_chart(avg_neighbour.set_index('host_neighbourhood'))
    
    #top host by total reviews
    st.subheader("Top 10 Reviews")    
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
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")     
    st.bar_chart(data=top_hotel_reviews.head(10),x='Hotel Name', y='Number of Reviews',horizontal=True,use_container_width=True)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")  
        
    #cancelation policy 
    st.subheader("Cancelation Policy")     
    cancel_policy = df['cancellation_policy'].value_counts().reset_index()
    cancel_policy.columns = ['cancellation_policy', 'count']
    st.dataframe(cancel_policy, use_container_width=True)
    fig1 = px.pie(cancel_policy, values='count', names='cancellation_policy', title='Cancellation Policy')
    st.plotly_chart(fig1)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")  
        
    #bedrooms 
    st.subheader("Bedrooms Types")     
    bedrooms = df['bedrooms'].value_counts().reset_index()
    bedrooms.columns = ['bedrooms', 'count']
    st.dataframe(bedrooms, use_container_width=True)
    fig2 = px.pie(bedrooms, values='count', names='bedrooms', title='Bedrooms types ')
    st.plotly_chart(fig2)

def func_others(value):
    df_csv = pd.read_csv("airbnbdata/airbnb.csv")
    df=pd.DataFrame(df_csv)

    filtered_df = df[df["host_neighbourhood"] == value]
        
    #average, sum of reviews
    filtered_df_mean = filtered_df["number_of_reviews"].mean().sum()
    filtered_df_sum =  filtered_df["number_of_reviews"].sum()
    col1,col2 = st.columns(2)
    with col1: 
      st.subheader("Average Reviews")         
    with col2:  
      st.subheader("Total Reviews")      
    
    col1.metric("",round(filtered_df_mean, 2))
    col2.metric("",filtered_df_sum)    

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    #count host neighbourhood
    filtered_list_neighbour = list(set(filtered_df["host_neighbourhood"]))
    filtered_df_count_neighbour =pd.Series(filtered_list_neighbour).value_counts().sum()
    #st.write("count of neighbourhood",filtered_df_count_neighbour)
    #count host id
    filtered_list_host_id = list(set(filtered_df["host_id"]))
    filtered_df_count_host_id =pd.Series(filtered_list_host_id).value_counts().sum()
    col3,col4 = st.columns(2)
    with col3: 
      st.subheader("Host Neighbourhood Count")          
    with col4:  
      st.subheader("Host ID Count")      
      
    col3.metric("",filtered_df_count_neighbour)
    col4.metric("",filtered_df_count_host_id)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ") 
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ") 

    #room type price
    filtered_room_types = filtered_df.groupby("room_type")[["price"]].sum()
    filtered_room_types.reset_index(inplace=True)
    filtered_df_room_types = filtered_room_types   
    
    #total room type price
    st.subheader("Total Price of Room Types")    
    filtered_tot_neighbour_room = filtered_df.groupby(["host_neighbourhood","room_type"])["price"].sum() 
    filtered_tot_neighbour_room = filtered_tot_neighbour_room.reset_index()
    cols = filtered_tot_neighbour_room.columns.tolist()
    cols[0], cols[1] = cols[1], cols[0]  # Swap 'host_neighbourhood' and 'room_type'
    filtered_tot_neighbour_room = filtered_tot_neighbour_room[cols]
    filtered_tot_neighbour_room_new = filtered_tot_neighbour_room.pivot(index='host_neighbourhood', columns='room_type', values='price')
    st.dataframe(filtered_tot_neighbour_room_new, use_container_width=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")    
    st.bar_chart(filtered_df_room_types.set_index('room_type'))
        
    #average price of neighbourhood
    st.subheader("Average Price of Host Neighbourhood")    
    filtered_avg_neighbour = filtered_df.groupby("host_neighbourhood")[["price"]].mean() 
    filtered_avg_neighbour.reset_index(inplace=True)
    st.dataframe(filtered_avg_neighbour.head(10), use_container_width=True) 
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")     
    st.bar_chart(filtered_avg_neighbour.set_index('host_neighbourhood'))
    
    #top host by total reviews
    st.subheader("Top 10 Reviews")    
    filtered_review_group = filtered_df[['name','country','review_scores','number_of_reviews']]
    filtered_review_group = filtered_review_group.reset_index(drop=True)
    filtered_top_hotel_reviews = filtered_review_group.sort_values(by=['review_scores', 'number_of_reviews'], ascending=[False, False])
    filtered_top_hotel_reviews = filtered_top_hotel_reviews.reset_index(drop=True)
    filtered_top_hotel_reviews = filtered_top_hotel_reviews.rename(columns={
    'name': 'Hotel Name', 
    'review_scores': 'Review Scores', 
    'number_of_reviews': 'Number of Reviews',
    'country':'Country Name'})
    st.dataframe(filtered_top_hotel_reviews.head(10), use_container_width=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")     
    st.bar_chart(data=filtered_top_hotel_reviews.head(10),x='Hotel Name', y='Number of Reviews',horizontal=True,use_container_width=True)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")  
        
    #cancelation policy 
    st.subheader("Cancelation Policy")     
    filtered_cancel_policy = filtered_df['cancellation_policy'].value_counts().reset_index()
    filtered_cancel_policy.columns = ['cancellation_policy', 'count']
    st.dataframe(filtered_cancel_policy, use_container_width=True)
    fig1 = px.pie(filtered_cancel_policy, values='count', names='cancellation_policy', title='Cancellation Policy')
    st.plotly_chart(fig1)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")  
        
    #bedrooms 
    st.subheader("Bedrooms Types")     
    filtered_bedrooms = filtered_df['bedrooms'].value_counts().reset_index()
    filtered_bedrooms.columns = ['bedrooms', 'count']
    st.dataframe(filtered_bedrooms, use_container_width=True)
    fig2 = px.pie(filtered_bedrooms, values='count', names='bedrooms', title='Bedrooms types ')
    st.plotly_chart(fig2)


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
        img1 = Image.open("airbnbdata/airbnblo.png")
        st.image( img1,width=600,channels="RGB" )
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        
        st.subheader("It’s easy to list your home on Airbnb")
        st.markdown("**Create a listing for your place in just a few steps**")
        st.markdown("**Go at your own pace, and make changes whenever**")
        st.markdown("**Get 1:1 support from experienced hosts at any time**")
        st.markdown(" ")
        
        img2 = Image.open("airbnbdata/airbnbmob.jpeg")
        st.image( img2,width=600,channels="RGB" )
        st.subheader("It’s easy to list your home on Airbnb")
        st.markdown("**Listing editor**")
        st.markdown(":gray[Showcase every detail of your home]")
        st.markdown("**Calendar**")
        st.markdown(":gray[Manage your availability and pricing]")
        st.markdown("**Messages**")
        st.markdown(":gray[Quickly message guests and support]")
        st.markdown(" ")
        
        img3 = Image.open("airbnbdata/airbnbhouse.jpeg")
        st.image( img3,width=600,channels="RGB" )
        st.write("click here to go [airbnb](https://www.airbnb.co.in/)")

elif select == "ANALYSIS":
        list_neighbour = list(set(df["host_neighbourhood"]))
        neighbourhood =  st.selectbox( "Select one", ["All"] + list_neighbour)
        if st.button("Submit"):
             if neighbourhood == "All":
                 func_all()
             else:
                 neighbourhood_name = neighbourhood
                 func_others(neighbourhood_name)  
       
