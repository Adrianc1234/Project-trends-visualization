# Libraries
from cgitb import text
from code import interact
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_position(2000,0)
driver.maximize_window()

#funciones

def log_in():

    #inicializamos el navegador
    driver.get('https://www.instagram.com/')
    username = "isabelmontalvo24"
    password = "pikapika22"
    l_user = "auronplay"
    #añadimos usuario y contraseña
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]'))).send_keys(username)
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]'))).send_keys(password)

    #Enter
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    time.sleep(10)
    driver.get(f'https://www.instagram.com/{l_user}')
    time.sleep(10)

def scroll_down():
    for i in range(0,6):
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def click_more():
    try:
        time.sleep(3)
        WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._a9-r'))).click()
        time.sleep(5)
    except:
        return False

def extract_html():
    #driver.get('https://www.instagram.com/')
    body = driver.execute_script("return document.body")
    source = body.get_attribute('innerHTML') 
    soup = BeautifulSoup(source, "html.parser")
    soup = soup.prettify().encode()
    with open('saving.html', 'wb+') as f:
        f.write(soup)
    #return soup.prettify() 

def extraction_massive(data):
    data_new = []
    p_info = []
    videos_info = []
    links_info = []
    counter = 0
    description = []
    profiles = []

    # info
    text_d = data.find('div',attrs={"class" : "_aa_c"})
    description.append(text_d.get_text().replace('\n','').strip())

    #info personal
    infos = data.find_all('li',attrs={"class" : "_aa_5"})
    for info in infos:
        p_info.append(info.get_text().replace('\n','').strip())
    
    #VIDEOS
    videos = data.find_all('svg',attrs={"aria-label" : "Clip"})
    videos_info.append(len(videos))

    #imagenes y videos
    #print(data)
    for feed in data:
        #print(feed)
        
        try:
            set1 = feed.find_all('img',attrs={"class" : "_aagt"})
            for item in set1:
                #print(item)
                try:
                    link = item["src"]
                    #print(link)
                    
                    date = item["alt"]
                    #print(date)
                    links_info.append([date,link])
                except:
                    continue
        except:
            continue

    #otros perfiles
    for feed2 in data:
        #print(feed)
        try:
            set2 = feed2.find_all('a',attrs={"role" : "link"})
            for item2 in set2:
                #print(item)
                try:
                    link_p = item2["href"]
                    #print(link_p)
                    profiles.append(link_p)
                except:
                    continue
        except:
            continue

            
    
    data_new = [description, p_info,videos_info,links_info,[len(links_info)],profiles]
    for i in data_new:
        print(i)
    
        

#clicks a todo el perfil
#log_in()
#scroll_down()
#extract_html()
with open('saving.html', 'rb') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
#print(soup)
#print(soup.find('div',attrs={"class" : "_aa_c"}))
#print(a)
#guardar el html con la informacion en un txt

extraction_massive(soup)

driver.close()
