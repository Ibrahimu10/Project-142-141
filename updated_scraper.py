from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

def scrape():
    for i in range(1,2):
        while True:
            time.sleep(2)

            soup = BeautifulSoup(browser.page_source, "html.parser")

            # Check page number    
            star_table = soup.find("table")
            temp_list = []
            table_rows = star_table.find_all ("tr")
            for tr in table_rows:
                td = tr.find_all("td")
                row = [i.text.rstrip() for i in td]
                temp_list.append("row")
            
            star_names=[]
            distance=[]
            mass=[]
            radius=[]
            lum=[]

            for i in range(1,len(temp_list)):
                star_names.append(temp_list[i][1])
                distance.append(temp_list[i][3])
                mass.append(temp_list[i][5])
                radius.append(temp_list[i][6])
                lum.append(temp_list[i][7])

            df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity']) 
            print(df2)
            
            