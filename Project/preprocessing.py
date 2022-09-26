#import the librarys we will using
from pandas import json_normalize
import re
from datetime import datetime
import json
import pandas as pd
import seaborn as sns
import numpy as np
from geopy.geocoders import Nominatim

# here we proceed to read the file in json format by dataframe of pandas
# and open json file we will work after

with open('scrapper.json') as jsonfile:
    data = json.load(jsonfile)
    df = pd.DataFrame([data])

#here we convert the dictionary to a pandas dataframe 
data1=pd.DataFrame.from_dict(data['posts_info'])

#here because of the way we get the data in posts_info we have to use 
#a transpose to be able to change the position of the rows by columns 
#and make it easier to handle and read.
data2=pd.DataFrame.transpose(data1)

#In this part we proceed to eliminate special characters, as well as 
#to adapt the corresponding data for its better use.
for i in range(len(data2['likes'])):
    data2['likes'][i] = str(data2['likes'][i]).replace("[]","0")
    data2['likes'][i] = str(data2['likes'][i]).replace("[","").replace("]","")
    data2['likes'][i] = str(data2['likes'][i]).replace("'","").replace("'","")
    data2['likes'][i] = str(data2['likes'][i]).replace(",","")
    #data2['likes'][i] = str(data2['likes'][i]).replace("['","").replace("']","").replace("[","").replace("]","")
    #data2['likes'][i] = str(data2['likes'][i]).replace("', '', '', '","")
    data2['likes'][i] = str(data2['likes'][i]).replace("'","")
    try:
        data2['likes'][i]=int(data2['likes'][i])
    except:
        data2['likes'][i] = 0
        
for i in range(len(data2['date'])):
    data2['date'][i] = str(data2['date'][i]).replace("[","").replace("]","")
    data2['date'][i] = str(data2['date'][i]).replace("'","").replace("'","")

#here we are going to break down the date for day, month and year in 
#order to be able to manipulate the information easier, using methods 
#like regex and datetime
for i in range(len(data2['date'])):
  match_str=re.search(r'\d{4}-\d{2}-\d{2}', str(data2['date'][i]))
  #print(match_str)
  # computed date
  # feeding format
  res = datetime.strptime(match_str.group(), '%Y-%m-%d').date()
  #print(res)
  data2['date'][i]=str(res)

year=[]
month=[]
day=[]

date_time=pd.to_datetime(data2['date'])

for i in range(len(data2['date'])):
    year.append(date_time.dt.year[i])
    month.append(date_time.dt.month[i])
    day.append(date_time.dt.day[i])


#In this part we proceed to eliminate special characters, as well as 
#to adapt the corresponding data for its better use.
for i in range(len(data2['photo'])):
    data2['photo'][i] = str(data2['photo'][i]).replace("[]","Others Media")
    data2['photo'][i] = str(data2['photo'][i]).replace("[","").replace("]","")
    data2['photo'][i] = str(data2['photo'][i]).replace("'","").replace("'","")

# Clean description photo
for i in range(len(data2['description_photo'])):
    data2['description_photo'][i] = str(data2['description_photo'][i]).replace("[]","Others Media")
    data2['description_photo'][i] = str(data2['description_photo'][i]).replace("[","").replace("]","")
    data2['description_photo'][i] = str(data2['description_photo'][i]).replace("'","").replace("'","")
    data2['description_photo'][i] = str(data2['description_photo'][i]).replace(""","").replace(""","")

#Once preprocessed we proceed to attach it to the new dataFrame.
df_general = pd.DataFrame({'username' : [], 'number_post' : [], 'number_followers' : [], 'number_followings' : [], 'photo_profile' : [],'real_name' : [],  'verified' : [], 'profession' : [],'description':[]})
df_general2 = pd.DataFrame({'id' : [], 'likes' : [], 'date' : [], 'year' : [], 'month' : [], 'day' : [], 'photo' : [],'url_post' : [],'location' : [],'description_photo' : [],})

df_general['username'] = df['username']
df_general['number_post'] = df['number_post']
df_general['number_followers'] = df['number_followers']
df_general['number_followings'] = df['number_followings']
df_general['photo_profile'] = df['real_name']
df_general['real_name'] = df['real_name']
df_general['verified'] = df['verified']
df_general['profession'] = df['profession']
df_general['description'] = df['description']


df_general2['id'] = data2['id']
df_general2['likes'] = data2['likes'] 
df_general2['date'] = data2['date']
df_general2['year'] = year
df_general2['month'] = month
df_general2['day'] = day
df_general2['photo'] = data2['photo']
df_general2['url_post'] = data2['url_post']
df_general2['location'] = data2['location']
df_general2['description_photo'] = data2['description_photo']


#here we are going to join the 2 dataframes that we have previously 
#preprocessed using a pandas method called concat
df_general3 =pd.concat([df[['number_followers','number_followings']], df], axis=1)

# Metrics

#Total Number of Post
#total_post=df_general2['id'].count()

#Total Number of likes
#total_likes=df_general2['likes'].sum()

#Average likes
#average_likes=df_general2['likes'].mean()

#Median likes
#median_likes=df_general2['likes'].median()

#df
#data_metrics = [{'Total posts': total_post, 'Total likes': total_likes, 'Average likes': average_likes, 'Median likes': median_likes}]
#df_metrics = pd.DataFrame(data_metrics)

# Location
latitude=[]
longitude=[]
location2=[]

for i in df_general2["location"]:
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(i)
    if i!=None:
        if(getLoc==None):
            #print("no se encontro")
            pass
        else:
            #print(getLoc.latitude)
            location2.append(str(i))
            long=getLoc.longitude
            lati=getLoc.latitude
            latitude.append(lati)
            longitude.append(long)


df_location= pd.DataFrame({'location': [],'latitude':[],'longitude':[], })

df_location["location"]=location2
df_location["latitude"]=latitude
df_location["longitude"]=longitude

# Convert dataframes to json
list_df = [df, df_general2, df_location]

with open("final_merged.json", 'w') as outfile:
    outfile.write(json.dumps([df.to_dict() for df in list_df]))

print("preprocessing finished.")