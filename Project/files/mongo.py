import datetime
from itertools import count
import json
import pandas as pd
import pymongo
from pymongo import MongoClient
from datetime import datetime as dt


#reordering our posts 
def tidy_data(data):
    id  = []
    likes = []
    date  = []
    year  = []
    month  = []
    day  = []
    photo = []
    url_post  = []
    location  = []
    description_photo = [] 

    for n in range(0, len(data[1]["id"])): 
        id.append(data[1]["id"][f'user_post{n}'])
        likes.append(data[1]["likes"][f'user_post{n}'])
        date.append(data[1]["date"][f'user_post{n}'])
        year.append(data[1]["year"][f'user_post{n}'])
        month.append(data[1]["month"][f'user_post{n}'])
        day.append(data[1]["day"][f'user_post{n}'])
        photo.append(data[1]["photo"][f'user_post{n}'])
        url_post.append(data[1]["url_post"][f'user_post{n}'])
        location.append(data[1]["location"][f'user_post{n}'])
        description_photo.append(data[1]["description_photo"][f'user_post{n}'])
    
    df = pd.DataFrame((zip(id,
        likes,
        date,
        year,
        month,
        day,
        photo,
        url_post,
        location,
        description_photo)), 
        columns = ['id',
        'likes', 
        'date', 
        'year', 
        'month', 
        'day', 
        'photo',
        'url_post', 
        'location', 
        'description_photo'])
    
    return df

def metrics(df):
    #Total Number of Post
    total_post=df['id'].count()
    
    #Total Number of likes
    total_likes=df['likes'].sum()
    
    #Average likes
    average_likes=df['likes'].mean()
    
    #Median likes
    median_likes=df['likes'].median()
    
    #amount of other types
    other_count = (df['photo']=='Others Media').value_counts()[True]

    #proportion btn unique photo and other types 
    photo_count = total_post - other_count

    #most liked other post
    max_post = df.loc[df.loc[:, 'photo'] == 'Others Media'].max()

    #count by days
    dates = df['date']
    dates_count = []
    count = 0
    likes_sum = {'Friday': 0, 'Sunday': 0, 'Tuesday': 0, 'Monday': 0, 'Wednesday': 0, 'Saturday': 0, 'Thursday': 0}
    likes_avg = {'Friday': 0, 'Sunday': 0, 'Tuesday': 0, 'Monday': 0, 'Wednesday': 0, 'Saturday': 0, 'Thursday': 0}
    total_dates = {'Friday': 0, 'Sunday': 0, 'Tuesday': 0, 'Monday': 0, 'Wednesday': 0, 'Saturday': 0, 'Thursday': 0}

    for i in dates:

        year, month, day= (int(x) for x in i.split('-'))
        ans = datetime.date(year, month, day)
        dates_count.append(ans.strftime("%A"))

        #total likes by day
        likes_date = df.loc[df.loc[:, 'id'] == count]
        likes_sum[ans.strftime("%A")] = likes_sum[ans.strftime("%A")] + int(likes_date['likes'])
        
        count += 1

    #reconteo de total dates
    total_dates2 = dict(zip(dates_count,map(lambda x: dates_count.count(x),dates_count)))
    for i in total_dates2:
        total_dates[i] = total_dates[i] + total_dates2[i] 
    print(total_dates)

    for item in likes_sum:
        try:
            likes_avg[item] = likes_sum[item] / total_dates[item]
        except:
            likes_avg[item] = 0

    return [{'Total posts': str(total_post),
    'Total likes': str(total_likes),
    'Average likes': str(average_likes),
    'Median likes': str(median_likes),
    'Other posts': str(other_count),
    'Photo count': str(photo_count),
    'Most liked': str(max_post['url_post']),
    'total day': total_dates,
    'total likes day': likes_sum,
    'avg likes day': likes_avg}]

def update(data):
    df = tidy_data(data)
    json_metrics = metrics(df)

    myclient = MongoClient("mongodb+srv://general:General2022..@cluster0.mfzpwpz.mongodb.net/?retryWrites=true&w=majority")

    # Calling the database from the cluster
    db = myclient["IGinstagram"]
    collection = db["scrapers"]

    # Sample data to add in the collection
    data = {"username": data[0]['username']['0'], "date_insertion": dt.today().strftime('%Y-%m-%d %H:%M'), "p_info": data[0], "data_frame": df.to_json(orient='columns'),"locations":data[2], "metrics":json_metrics}
    collection.insert_one(data)

def check(username):

    myclient = MongoClient("mongodb+srv://general:General2022..@cluster0.mfzpwpz.mongodb.net/?retryWrites=true&w=majority")

    # Calling the database from the cluster
    db = myclient["IGinstagram"]
    collection = db["scrapers"]
    r = []
    for i in collection.find({"username": username}):
        r.append(i)
    
    #verificamos existencia
    if len(r)>=1:
        return True
    else:
        return False

def check(username):
    myclient = MongoClient("mongodb+srv://general:General2022..@cluster0.mfzpwpz.mongodb.net/?retryWrites=true&w=majority")

    # Calling the database from the cluster
    db = myclient["IGinstagram"]
    collection = db["scrapers"]
    for i in collection.find({"username": username}):
        print(i)
    

