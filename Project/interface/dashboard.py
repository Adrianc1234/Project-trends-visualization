#dashboard with streamlit
from pickle import GLOBAL
import re
import streamlit as st
import pandas as pd
import numpy as np
import time 
from datetime import date
import matplotlib.pyplot as plt
import pymongo
from pymongo import MongoClient
import requests
from PIL import Image

# Instagram dashboard
# multi page app with streamlit 
# page change with button condition


# page settings
st.set_page_config(page_title = "Instagram Dashboard",
    page_icon = "📷",
    layout = "wide")

# style
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def check(username):

    myclient = MongoClient("mongodb+srv://general:General2022..@cluster0.mfzpwpz.mongodb.net/?retryWrites=true&w=majority")

    # Calling the database from the cluster
    db = myclient["IGinstagram"]
    collection = db["scrapers"]
    r = []
    for i in collection.find({"username": username}):
        #print(i['username']) #ejemplo de uso para acceder a la info
        #print(i['metrics']) #ejemplo 2 de uso para acceder a la info
        return i['metrics'], i['p_info'], i['locations'], i['username']


#LLAVES DEL DIC
#_id
#username
#date_insertion
#p_info
#data_frame
#locations
#metrics


db_metrics, db_info, db_location, db_username = check("auronplay")
#print(db[0]['Average likes'])
print(db_info)

url_imagen = (db_info['photo_profile']['0'][0]) # El link de la imagen
nombre_local_imagen = "profile.jpg" # El nombre con el que queremos guardarla
imagen = requests.get(url_imagen).content
with open(nombre_local_imagen, 'wb') as handler:
    handler.write(imagen)

# access to username from database


# page 1
def requirements():
    #instagram logo centered
    st.markdown('''
        <div class="container2">
        ''', unsafe_allow_html=True)
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png', width=200)
    st.title('Instagram Dashboard')
    st.subheader('By: Datastar 🪐')
    st.markdown('''
    To findout everything about an Instagram account you will need:
    - Public account or account that you are following
    - Your profile without double autentication
    - Account with visible like number on posts

    *This dashboard will show you the insights of the account for their last 50 posts*
    ''')

    st.markdown(''' ### Enter your credentials''')
    personal_username = st.text_input('Your username', '@your_username', key = 'your_username')
    personal_password = st.text_input('Your password', 'your_password', key = 'your_password')

    # enter username to get insights
    username = st.text_input('Enter username for insights', '@example', key = 'username')

    # validate username with button
    def validate_username(username_To_validate):
        if len(username_To_validate) == 0 or '@' not in username_To_validate:
            st.error(f'This user name is not valid')
            return False
        elif username_To_validate == '@example':
            st.error('Please enter a username')
            return False
        elif username_To_validate == '@your_username':
            st.error('Please enter your username')
            return False
        else:
            return True

    # button to go to page 2
    if st.button('Go'):
        if validate_username(personal_username):
            if validate_username(username):
                with st.spinner('Scrapping the data...'):
                    #here we need to scrape the data
                    time.sleep(3)
                st.balloons()
                dashboard(username)
                return username, True


    


# page 2
def dashboard(username):
    st.sidebar.title('Filters')
    
    all_posts = st.sidebar.checkbox('All posts', value = True)
    # title 
    col1, col2 = st.columns([5, 1])
    with col1:
        
        st.title('Instagram Dashboard of {}'.format(username))
    with col2:
        # verificado si aplica
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)

        st.image('https://i.pinimg.com/736x/5c/6a/99/5c6a9983d0c9eef8b3912a451cc8a27d.jpg', width=40)
    # insights
    col3, col4, col5, col6 = st.columns(4)

    with col3:
        #add profile picture
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)

        image = Image.open('profile.jpg')
        st.image(image, width=200)
        

    with col4:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Followers', '1.2K')

    with col5:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Following', '200')
    
    with col6:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Posts', str(db_metrics[0]['Total posts']))

    # bio
    st.markdown('''This is the bio of the account''')

    col7, col8 = st.columns([2, 1])
    with col7:

        if all_posts:
            st.markdown(''' ## Likes per post''')

        else:
            # line chart with likes and comments 
            date_to_filter = st.sidebar.slider('month',
                                                value=date(2020, 1, 1),
            format="MM/DD/YY")

            #Update title based on the slider.
            st.markdown('''## Likes per post in {}'''.format(date_to_filter))

    with col8:
        st.markdown('''## \#1 Post''')

    col9, col10 = st.columns([2, 1])

    with col9:

        # dataframe with random date and likes
        chart_data = pd.DataFrame(
        np.random.randn(20),
        columns=['likes'])


        if all_posts:
            #st.markdown(''' ## Likes per post''')
            st.line_chart(chart_data)

        else:
            # line chart with likes and comments 
           # date_to_filter = st.sidebar.slider('month',
             #                                   value=date(2020, 1, 1),
            #format="MM/DD/YY")

            #Update title based on the slider.
            #st.title('Likes and comments per post in {}'.format(date_to_filter))
            

            #Plot only points at the hour given by the slider.
            #filter_data = data[data["date/time"].dt.month == [month_to_filter]

            #here we need to filter the data
            st.line_chart(chart_data)
    
    with col10:
        # most liked post
        st.markdown('''
        <div class="container2">
        ''', unsafe_allow_html=True)
        print(str(db_metrics[0]['Most liked']))
        st.image(str(db_metrics[0]['Most liked']), width=200)


    # insights
    col11, col12 = st.columns(2)

    with col11:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.markdown('''## Likes''')

    with col12:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.markdown('''## Single photo vs other media''')


    col13, col14, col15, col16, col17, col18 = st.columns(6)

    with col13:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Total', str(db_metrics[0]['Total likes']))

    with col14:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Average', str(db_metrics[0]['Average likes']))
    
    with col15:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Median', str(db_metrics[0]['Median likes']))

    with col16:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Single Photos', str(db_metrics[0]['Photo count']))

    with col17:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Other Posts', str(db_metrics[0]['Other posts']))
    
    with col18:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
       


    col19, col20 = st.columns([3,1])

    with col19:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.markdown('''## Locations''')

    with col20:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.markdown('''## Top 5''')

    col21, col22 = st.columns([2,1])
  
    with col21:
        # df with random location 
        df2 = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [20.97, -89.62],
        columns=['lat', 'lon'])

        st.map(df2)
    
    with col22:
    
        np.random.seed(19680801)

        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        y_pos = np.arange(len(people))
        performance = 3 + 10 * np.random.rand(len(people))
        error = np.random.rand(len(people))

        ax.barh(y_pos, performance, xerr=error, align='center')
        ax.set_yticks(y_pos, labels=people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Performance')
        ax.set_title('How fast do you want to go today?')

        st.pyplot(fig)

    
#requirements()
dashboard('auronplay')