#dashboard with streamlit
from pickle import GLOBAL
import re
import streamlit as st
import pandas as pd
import numpy as np
import time 
from datetime import date
import matplotlib.pyplot as plt

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


# page 1
def requirements():
    #instagram logo centered
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
        if validate_username(username):
            if validate_username(personal_username):
                with st.spinner('Scrapping the data...'):
                    #here we need to scrape the data
                    time.sleep(5)
                st.balloons()
                dashboard(username)
                return username, True


    


# page 2
def dashboard(username):
    st.sidebar.title('Filters')
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
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        #add profile picture

        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png', width=100)

    with col2:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Followers', '1.2K')

    with col3:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Following', '200')
    
    with col4:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Posts', '200')

    # bio
    st.markdown('''This is the bio of the account''')

    col5, col6 = st.columns([2, 1])
    with col5:
        # posts
        all_posts = st.sidebar.checkbox('All posts', value=True)

        if all_posts:
            st.markdown(''' ## Likes per post''')
            

        else:
            # line chart with likes and comments 
            date_to_filter = st.sidebar.slider('month',
                                                value=date(2020, 1, 1),
            format="MM/DD/YY")

            #Update title based on the slider.

            st.markdown('''## Likes per post in {}'''.format(date_to_filter))

    with col6:
        st.markdown('''## \#1 Post''')

    col5, col6 = st.columns([2, 1])

    with col5:

        # dataframe with random date and likes
        chart_data = pd.DataFrame(
        np.random.randn(20),
        columns=['likes'])

        all_posts = st.sidebar.checkbox('All posts', value=True, key='all_posts')

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

            #here we need to filter the datar
            st.line_chart(chart_data)
    
    with col6:
        # most liked post
        st.markdown('''
        <div class="container2">
        ''', unsafe_allow_html=True)
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png', width=200)


    # insights
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.markdown('''## Likes''')

    with col2:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.markdown('''## Other insights''')


    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Total', '1.2K')

    with col2:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Average', '200')
    
    with col3:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Median', '200')

    with col4:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Total', '1.2K')

    with col5:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Average', '200')
    
    with col6:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Median', '200')


    col7, col8 = st.columns([3,1])

    with col7:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.markdown('''## Locations''')

    with col8:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.markdown('''## Top 5''')

    col9, col10 = st.columns([2,1])
  
    with col9:
        # df with random location 
        df2 = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [20.97, -89.62],
        columns=['lat', 'lon'])

        st.map(df2)
    
    with col10:
    
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


    
    
requirements()