# Libraries
import time

from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Instagram_Scrap:

    def __init__(self,username): 
        self.username = username
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options = options)

    def close(self):
        """Close the browser."""
        self.driver.close()

    def login(self):
        """ 
        Function login in to Instagram.
        
        Write the bot credentials or your password, we need it to navigate in the profile pages
        """

        credentials = dict()
        credentials['username']='adrianrobertocarmona@hotmail.com'
        credentials['password']='HALO2015..'

        print('\nLogging in…')
        self.driver.get('https://www.instagram.com')

        time.sleep(random.randint(2, 5))

        # Click in the buttons
        us = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]')))
        time.sleep(random.randint(2, 4))
        pa = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]')))
        time.sleep(random.randint(2, 4))

        us.clear()
        us.send_keys(credentials['username'])
        pa.clear()
        pa.send_keys(credentials['password'])
        Login_button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        
        '''
        In case you want to close the pop up window but it's not necessary in this case 

        '''
        #print('pre not_now')
        # time.sleep(15)
        #not_now = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.cmbtv button'))).click()
        #print('post not_now')
        #time.sleep(10)
        #not_now = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div._a9-z button[class="_a9-- _a9_1"]'))).click()
        
        print('We finish the loggin in')

    def go_to_profile(self):
        time.sleep(5)
        '''
        Function to go to the profile
        
        '''

        url = 'https://www.instagram.com/'
        profile_name = self.username #str(input('Write the username:   '))
        final_url = url + profile_name
        self.driver.get(final_url)

        return profile_name


    def extract_links_post(self):
        reached_page_end = False
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        links=set()
        while not reached_page_end:   
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # Fetching Posts
            posts = self.driver.find_elements(By.CSS_SELECTOR, 'div._aabd._aa8k._aanf a')

            fetched_links = [post.get_attribute("href") for post in posts]

            links = links.union(set(fetched_links))

            if last_height == new_height or len(links) >= 36:
                reached_page_end = True
            else:
                last_height = new_height

        return list(links)
        
    def get_photos(self):
    
        time.sleep(2)
        photos_aux = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="_aagu"] img')
        photos_final = [node.get_attribute('src') for node in photos_aux]
        description_photo = [node.get_attribute('alt') for node in photos_aux]

        return photos_final, description_photo


    def extract_info_profile(self):
        time.sleep(3)
        profile_info = self.driver.find_elements(By.CSS_SELECTOR, 'li._aa_5 div._aacl._aacp._aacu._aacx._aad6._aade span')
        profile_info_final = [node.text for node in profile_info]

        name_user = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="_aa_c"] span._aacl')
        name_user_final = [node.text for node in name_user]

        description = self.driver.find_elements(By.CSS_SELECTOR, 'div._aa_c div[class="_aacl _aacp _aacu _aacx _aad6 _aade"]')
        description_final = [node.text for node in description]

        if len(description_final) != 0:
            description_final = description_final[0]
        else:
            description_final = None


        try:
            verified = self.driver.find_elements(By.CSS_SELECTOR,'div[class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _abb0 _abcm"] span[class="_act0 _a9_u _9ys7"]')
            verified = [node.text for node in verified]
            verified = verified[0]
            verified = True
        except:
            verified = False

        try:
            profession = self.driver.find_elements(By.CSS_SELECTOR,'div[class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm"] div[class="_aacl _aacp _aacu _aacy _aad6 _aade"]')
            profession_final = [node.text for node in profession]
            profession_final = profession_final[0]
        except:
            profession_final = None

        profile_photo_aux = self.driver.find_elements(By.CSS_SELECTOR, 'div._aarf._aarg span img')
        profile_photo = [node.get_attribute('src') for node in profile_photo_aux]
        

        return profile_info_final, profile_photo , name_user_final, description_final, verified, profession_final


    def srcset_filter(self, srcset):
        newUrls = []

        try:
            for item in srcset:
                n_data = item.split(",")
                newUrls.append(n_data[0][0:n_data[0].index(" ")])
        except:
            return newUrls

        return newUrls

    def extract_info_post(self):

        links_post = self.extract_links_post()
        print(links_post,len(links_post))
        #photos, description_photo = self.get_photos()
        photos = []
        description_photos = []

        print('Extracting posts. Estimated time: ', 6*len(links_post))

        number_likes_list = []
        dates = []
        location_list = []

        for post in links_post:
            self.driver.get(post)
            time.sleep(6)

            try:
                likes = self.driver.find_elements(By.CSS_SELECTOR, 'div._ab8w a div._aacl span')
                number_likes_list_final = [node.text for node in likes]
                likes_final = number_likes_list_final[-1]
                number_likes_list.append(likes_final)
            except:
                likes_final = 0
                number_likes_list.append(likes_final)

            
            date = self.driver.find_elements(By.CSS_SELECTOR,'time._aaqe')
            dates_final = [node.get_attribute('datetime') for node in date]
            dates.append(dates_final)

            try:
                location = self.driver.find_elements(By.CSS_SELECTOR, 'div._aacl._aacn._aacu._aacy._aada._aade a')
                location_list_final = [node.text for node in location]
                location_list.append(location_list_final[0])
            except:
                location_list.append(None) 


            photo_fetched = False

            # 1 photo
            try:
                photo_aux = self.driver.find_elements(By.CSS_SELECTOR, 'div._aagu._aato div img') 
                photos_final_aux = [node.get_attribute('src') for node in photo_aux] 
                description_photo = [node.get_attribute('alt') for node in photo_aux] 
                photos_final = photos_final_aux[0]
                photo_fetched = True
            except:
                print("src was not matched")
                photos_final = None
                pass

            if photo_fetched != True:
                try:
                    photo_aux = self.driver.find_elements(By.CSS_SELECTOR, 'div._aagu._aato div img') 
                    photos_final_aux = [node.get_attribute('srcset') for node in photo_aux] 
                    description_photo = [node.get_attribute('alt') for node in photo_aux] 
                    photos_final_ = photos_final_aux[0]
                    photos_final = self.srcset_filter(photos_final_)
                    photo_fetched = True
                except:
                    photos_final = None
                    print("srcset was not matched")
                    pass

            # 2 or more photos
            if photo_fetched != True:
                try:
                    photo_aux = self.driver.find_elements(By.CSS_SELECTOR, 'div._aagu._aa20 div._aagv img') 
                    photos_final_aux = [node.get_attribute('srcset') for node in photo_aux] 
                    description_photo = [node.get_attribute('alt') for node in photo_aux] 
                    photos_final_ = photos_final_aux[0]
                    photos_final = self.srcset_filter(photos_final_)
                    photo_fetched = True
                except:
                    photos_final = None
                    print("Two photos or more")
                    pass

            
            if photo_fetched != True:
            # 2 or more photos
                try: 
                    photo_aux = self.driver.find_elements(By.CSS_SELECTOR, 'div._aagu._aamh div img')
                    photos_final_aux = [node.get_attribute('srcset') for node in photo_aux] 
                    photos_final_ = photos_final_aux
                    photos_final = self.srcset_filter(photos_final_)
                    description_photo = [node.get_attribute('alt') for node in photo_aux] 
                    photo_fetched = True
                except:
                    print("Video")
                    photos_final = None
                    pass

            photos.append(photos_final)
            description_photos.append(description_photo)

        return number_likes_list, dates, photos, description_photos, links_post, location_list

    def close(self):
        """Close the browser."""

        self.driver.close()