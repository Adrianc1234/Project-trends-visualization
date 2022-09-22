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
from math import pi
import main as m
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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
        return i['metrics'], i['p_info'], i['locations'], i['username'],i['data_frame']


#LLAVES DEL DIC
#_id
#username
#date_insertion
#p_info
#data_frame
#locations
#metrics


#db_metrics, db_info, db_location, db_username, db_dataframe = check(username)

"""
metric_graph = []
days = ['Friday','Sunday','Tuesday','Monday','Wednesday','Saturday','Thursday']
for i in days:
    fila = [i,db_metrics[0]['total likes day'][i], db_metrics[0]['avg likes day'][i]]
    metric_graph.append(fila)
df_likes = pd.DataFrame(metric_graph, columns=['day','t_likes_day', 'avg_likes_day'])
print(df_likes)

df_test = pd.DataFrame({
'group': ['t_likes_day','avg_likes_day'],
'Monday': [db_metrics[0]['total likes day']['Monday'],db_metrics[0]['avg likes day']['Monday']],
'Thursday': [db_metrics[0]['total likes day']['Thursday'],db_metrics[0]['avg likes day']['Thursday']],
'Wednesday': [db_metrics[0]['total likes day']['Wednesday'],db_metrics[0]['avg likes day']['Wednesday']],
'Tuesday': [db_metrics[0]['total likes day']['Tuesday'],db_metrics[0]['avg likes day']['Tuesday']],
'Friday': [db_metrics[0]['total likes day']['Friday'],db_metrics[0]['avg likes day']['Friday']],
'Saturday': [db_metrics[0]['total likes day']['Saturday'],db_metrics[0]['avg likes day']['Saturday']],
'Sunday': [db_metrics[0]['total likes day']['Sunday'],db_metrics[0]['avg likes day']['Sunday']]
})

print(df_test)


########################################################
# number of variable
categories=list(df_test)[1:]
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([2000000,4000000,6000000,8000000,10000000], ["1","2","3","4","5"], color="grey", size=7)
plt.ylim(0,40)
 

# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't make a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
values=df_test.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="group A")
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
values=df_test.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="group B")
ax.fill(angles, values, 'r', alpha=0.1)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Show the graph
plt.savefig("img.png")

############################################


url_imagen = (db_info['photo_profile']['0'][0]) # El link de la imagen
nombre_local_imagen = "profile.jpg" # El nombre con el que queremos guardarla
imagen = requests.get(url_imagen).content
with open(nombre_local_imagen, 'wb') as handler:
    handler.write(imagen)
"""
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
                
                m.execute(username.replace('@',""))
                st.balloons()
                dashboard(username.replace('@',""))
                return username, True


    


# page 2
def dashboard(username):
    db_metrics, db_info, db_location, db_username, db_dataframe = check(username)
    #overwrite image
    print(db_info['photo_profile']['0'][0])
    url_imagen = (db_info['photo_profile']['0'][0]) # El link de la imagen
    nombre_local_imagen = "profile.jpg" # El nombre con el que queremos guardarla
    imagen = requests.get(url_imagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)

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
        if db_info['verified']['0'] == True:
            
            st.image('https://i.pinimg.com/736x/5c/6a/99/5c6a9983d0c9eef8b3912a451cc8a27d.jpg', width=50)
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
        st.metric('Followers', db_info['number_followers']['0'])

    with col5:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Following', db_info['number_followings']['0'])
    
    with col6:
        st.markdown('''
        <div class="container">
        ''', unsafe_allow_html=True)
        st.metric('Posts', str(db_metrics[0]['Total posts']))

    # bio
    st.markdown('''### {}'''.format(db_info['real_name']['0'][0]))
    st.markdown('''### {}'''.format(db_info['profession']['0']))
    st.markdown('''{}'''.format(db_info['description']['0']))

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
        #plot likes per picture
        chart_data = pd.read_json(db_dataframe)


        if all_posts:
            #st.markdown(''' ## Likes per post''')
            st.line_chart(chart_data['likes'])

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

    
    col21, col22 = st.columns([2,1])
  
    with col21:
        # df with random location 
        dir = []
        for i in range(0,len(db_location['location'])):
            arr = [db_location['location'][str(i)], db_location['latitude'][str(i)], db_location['longitude'][str(i)]]
            dir.append(arr)
        df_loc = pd.DataFrame(dir, columns=['location','lat', 'lon'])
        #print(df_loc)

        st.map(df_loc)
    
    with col22:
        
        st.dataframe(df_loc['location'])

requirements()