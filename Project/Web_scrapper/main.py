from scrapper import Instagram_Scrap
import json
import os
import mongo as mg 
import getpass
import datetime
from datetime import datetime as dt

def execute(username):
    #password = getpass.getpass('Password: ')

    #condition
    if mg.check(username) == False:
        #Logging in 
        web = Instagram_Scrap(username)
        web.login()


        #Go to the desired profile
        username = web.go_to_profile()

        # Extract number of posts, followers and followings
        info, profile_photo ,name, description,verified, profession_final = web.extract_info_profile()


        # Extract general info of the profile: photos, number of likes, date
        number_likes_list, dates, photos, description_photo, links_post, location_list, = web.extract_info_post()

        #It closes the browser
        web.close()


        # Saving the information

        user = dict()


        user['username'] = username
        user['number_post'] = info[0]
        user['number_followers'] = info[1]
        user['number_followings'] = info[2]
        user['photo_profile'] = profile_photo
        user['real_name'] = name
        user['description'] = description
        user['verified'] = verified
        user['profession'] = profession_final



        user_posts = dict()
        print(len(number_likes_list) , len(photos))

        for i in location_list:
            print(i)
            
        for i in range(len(photos)):

            
            user_posts[f'user_post{i}'] = {}

            user_posts[f'user_post{i}']['id'] = i
            user_posts[f'user_post{i}']['likes'] = (number_likes_list[i])
            user_posts[f'user_post{i}']['date'] = dates[i]
            user_posts[f'user_post{i}']['photo'] = photos[i]
            user_posts[f'user_post{i}']['description_photo'] = description_photo[i]
            user_posts[f'user_post{i}']['url_post'] = links_post[i]
            user_posts[f'user_post{i}']['location'] = location_list[i]

        user['posts_info'] = user_posts
        print(user)
            

        with open("scrapper.json", "w") as outfile:
            json.dump(user, outfile)

        print("Extraction finished.")
        #execute the preprocess to generate our file
        try:
            os.system("python3 preprocessing.py")
        except:
            pass

        #leemos el archivo
        with open('final_merged.json') as jsonfile:
            data = json.load(jsonfile)
        
        #update
        print("Pushing...")
        mg.update(data)
        print("Pushed")

    else:
        print("existe")
        #os.system("python3 preprocessing.py")
    

