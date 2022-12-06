from locale import D_FMT
from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd

START_URL='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'    
page=requests.get(START_URL)  

soup=BeautifulSoup(page.text,"html.parser")
headers=['name','distance','mass','radius']
table_tag=soup.find('table')
temp_list=[]
table_rows=table_tag.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
name=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df=pd.DataFrame(list(zip(name,distance,mass,radius)),columns=['name','distance','mass','radius'])
df.to_csv('projet_output.csv')

