#dashboard with streamlit
import streamlit as st
import pandas as pd
import numpy as np
import time 
from datetime import date


# Instagram dashboard
# multi page app with streamlit 
# page change with button condition


# page 1
def requirements():
    #instagram logo centered
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png', width=200)
    st.title('Instagram Dashboard')
    st.subheader('By: Datastar 🪐')
    st.markdown('''
    To findout everything about an Instagram account you will need:
    - Public account
    - Profile without double autentication
    - Account with visible like number on posts
    ''')

    # enter username
    username = st.text_input('Enter username', '@example')
    # button to go to page 2
    if st.button('Go'):
        # if username is empty
        if username == '':
            st.error('Please enter a username')
        elif username == '@example':
            st.error('Please enter a username')
        else:
            st.write('You entered:', username)
            dashboard(username)

# page 2
def dashboard(username):
    st.sidebar.title('Filters')
    # title 
    st.title('Instagram Dashboard of {}'.format(username))
    # insights
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.header("Followers")
        st.title("1.2M")

    with col2:
        st.header("Posts")
        st.title("1.2K")

    with col3:
        st.header("Likes")
        st.title("1.2M")
    
    with col4:
        st.header("Comments")
        st.title("1.2K")

    # dataframe with random date and likes
    chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['likes', 'comments'])

    all_posts = st.sidebar.checkbox('All posts', value=True)

    if all_posts:
        st.title('Likes and comments per post')
        st.line_chart(chart_data)

    else:
        # line chart with likes and comments 
        date_to_filter = st.sidebar.slider('month',
                                            value=date(2020, 1, 1),
        format="MM/DD/YY")

        #Update title based on the slider.
        st.title('Likes and comments per post in {}'.format(date_to_filter))
        

        #Plot only points at the hour given by the slider.
        #filter_data = data[data["date/time"].dt.hour == hour_to_filter]

        #st.map(filter_data)

        
        #here we need to filter the datar
        st.line_chart(chart_data)


    # insights
    col1, col2 = st.columns(2)

    with col1:
        st.header("Most liked post")
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png', width=200)

    with col2:
        st.header("Most commented post")
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png', width=200)

    
    st. title('Likes insights')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Unique")
        st.title("1.2K")

    with col2:
        st.header("Average")
        st.title("1.2K")
    
    with col3:
        st.header("Median")
        st.title("1.2K")


    st. title('Comments insights')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Unique")
        st.title("1.2K")
    
    with col2:
        st.header("Average")
        st.title("1.2K")
    
    with col3:
        st.header("Median")
        st.title("1.2K")

    st.title('Location of posts')
    # df with random location 
    df2 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [20.97, -89.62],
    columns=['lat', 'lon'])

    st.map(df2)
    
    
requirements()
