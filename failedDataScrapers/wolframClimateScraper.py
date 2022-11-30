from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy as np
import csv
import pandas as pd

delay = 10

def getClimateDataOnScreen(driver, url):

	driver.get(url)
	
	# getting all data on screen
	time.sleep(12)
	driver.find_element(By.CSS_SELECTOR, '#__next > div > div._1MeJ._3eup > main > div._3BQG > div._2ThP > div._pA1m > section > section:nth-child(5) > header > ul > li:nth-child(1) > div > button > svg > path').click()
	driver.find_element(By.CSS_SELECTOR, '#__next > div > div._1MeJ._3eup > main > div._3BQG > div._2ThP > div._pA1m > section > section:nth-child(5) > header > ul > li:nth-child(1) > div > ul > li:nth-child(7) > button > span').click()
	time.sleep(1)
	driver.find_element(By.CSS_SELECTOR, '#__next > div > div._1MeJ._3eup > main > div._3BQG > div._2ThP > div._pA1m > section > section:nth-child(5) > header > ul > li:nth-child(3) > button > span').click()
	time.sleep(2)





driver = webdriver.Chrome()
hikes = np.genfromtxt('jamieHikes_lat_long.csv', delimiter = ',', dtype = None, encoding = None)
for i, hike in enumerate(hikes):
	if i == 0:
		temp = ['avg_temp']
		humidity = ['avg_humidity']
		windSpeed = ['avg_wind_speed']
	else:
		getClimateDataOnScreen(driver, 'https://www.wolframalpha.com/input?i=average+weather+latitude+' + hike[5] + '+longitude+' + hike[6])
		print(i)
driver.quit()



































