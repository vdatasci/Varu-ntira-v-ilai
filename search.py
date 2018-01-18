import pandas as pd
from bs4 import BeautifulSoup
import requests


for i in range(0, 606231):
    url = 'http://www.weatherbase.com/weather/weather.php3?s=' + str(i)
    
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    
    #create pandas dataframe with aggregated data from weatherbase.com


