from scrapper import Instagram_Scrap
import json


#Logging in 
web = Instagram_Scrap()
web.login()


#Go to the desired profile
username = web.go_to_profile()

# Extract number of posts, followers and followings
info, name, description,verified, profession_final = web.extract_info_profile()

print('Description:', description)

# Extract general info of the profile: photos, number of likes, date
number_likes_list, dates, photos = web.extract_info_post()

#It closes the browser
web.close()


# Saving the information

user = dict()


user['username'] = username
user['number_post'] = info[0]
user['number_followers'] = info[1]
user['number_followings'] = info[2]
user['real_name'] = name
user['description'] = description
user['verified'] = verified
user['profession'] = profession_final



user_posts = dict()
print(len(number_likes_list) , len(photos))

for i in range(len(photos)):
    user_posts[f'user_post{i}'] = {}

    user_posts[f'user_post{i}']['id'] = i
    user_posts[f'user_post{i}']['likes'] = (number_likes_list[i])
    user_posts[f'user_post{i}']['date'] = dates[i]
    user_posts[f'user_post{i}']['photo'] = photos[i]

user['posts_info'] = user_posts
print(user)
    

with open("scrapper.json", "w") as outfile:
    json.dump(user, outfile)










