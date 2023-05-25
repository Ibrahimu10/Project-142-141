from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

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
            table_rows = star_table[7].find_all ("tr")
            for tr in table_rows:
                td = tr.find_all("td")
                row = [i.text.rstrip() for i in td]
                temp_list.append("row")
            
            star_names=[]
            distance=[]
            mass=[]
            radius=[]

            for i in range(1,len(temp_list)):
                star_names.append(temp_list[i][0])
                distance.append(temp_list[i][5])
                mass.append(temp_list[i][7])
                radius.append(temp_list[i][8])

            df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius,)),columns=['Star_name','Distance','Mass','Radius']) 
            print(df2)
            df2.to_csv('dwarf_stars.csv')
            
            