from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy as np
import undetected_chromedriver.v2 as uc

driver = webdriver.Chrome()
login_url = "http://www.alltrails.com"
master_url = "https://www.alltrails.com/parks/canada/ontario/bon-echo-provincial-park"
# usr = 
# pwd = 

def login(driver, login_url, usr, pwd):

	driver = uc.Chrome()
	# driver.get(login_url)
	usr_in = driver.find_element_by_name(userEmail)
	usr_in.send_keys(usr)

	pwd_in = driver.find_element_by_name(userPassword)
	pwd_in.send_keys(pwd)
	pwd_in.submit

	driver.find_element_by_xpath('//*[@id="login-form"]/input').click()


def getTrailUrls(driver, master_url):
	driver.get(master_url)

	load_more_btn = driver.find_element_by_xpath('//*[@id="stick-bar-parent"]/div[2]/div[2]/button')
	print(driver.find_element_by_xpath('//*[@id="stick-bar-parent"]/div[2]/div[2]/div'))
	page_results = driver.find_element_by_xpath('//*[@id="stick-bar-parent"]/div[2]/div[2]/div').getText().split(" ")
	trails_total_num = page_results[6]
	trails_on_screen = page_results[4]

	while trails_on_screen != trails_total_num:
		load_more_btn.click()
		# time.sleep(1)
		trails_on_screen = driver.find_element_by_xpath('//*[@id="stick-bar-parent"]/div[2]/div[2]/div').getText().split(" ").page_results[4]

	trail_urls = []
	trail_e_list = driver.find_element_by_xpath('//*[@id="stick-bar-parent"]/div[2]/div[1]/div/div/a[1]')
	for trail_e in trail_e_list:
		trail_urls.append(trail_e.get_attribute("href"))

	return trail_urls


def scrape_trails(driver, trail_urls):

	#inserting header
	trail_data = [[length, elevation_gain, route_type, month, country, province_state, park, region, waterfall, views, lake, river, forest, hot_springs, cave, is_jamie, rating]]

	for i, url in enumerate(trail_urls):
		driver.get(url)
		# time.stop(1)
		trail_common_details = []

		##### getting trail details common to each month

		#length in km
		trail_common_details.append(
			driver
			.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/article/section[2]/div/span[1]/span[2]')
			.getText()
			.split(" ")[0])

		#elevation gain in m
		trail_common_details.append(
			driver
			.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/article/section[2]/div/span[2]/span[2]')
			.getText
			.split(" ")[0])

		#route type
		trail_common_details.append(
			driver
			.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/article/section[2]/div/span[3]/span[2]')
			.getText
			.split(" ")[0])

		#country
		trail_common_details.append(
			driver
			.find_element_by_xpath('//*[@id="breadcrumb-list"]/li[1]/a/span')
			.getText
			.split(" ")[0])

		#province/state
		trail_common_details.append(
			driver
			.find_element_by_xpath('//*[@id="breadcrumb-list"]/li[2]/a/span')
			.getText
			.split(" ")[0])

		#region
		trail_common_details.append(
			driver
			.find_element_by_xpath('//*[@id="breadcrumb-list"]/li[3]/a/span')
			.getText
			.split(" ")[0])

		boolean_attributes = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/article/section[3]/span/span')
		for boolean_attribute in boolean_attributes:
			boolean_attribute_text = boolean_attribute.getText()

			#waterfall
			if boolean_attribute_text == "Waterfall":
				trail_common_details.append(1)
			else:
				trail_common_details.append(0)

			#views
			if boolean_attribute_text == "Views":
				trail_common_details.append(1)
			else:
				trail_common_details.append(0)

			#lake
			if boolean_attribute_text == "Lake":
				trail_common_details.append(1)
			else:
				trail_common_details.append(0)

			#river
			if boolean_attribute_text == "River":
				trail_common_details.append(1)
			else:
				trail_common_details.append(0)

			#forest
			if boolean_attribute_text == "Forest":
				trail_common_details.append(1)
			else:
				trail_common_details.append(0)

			#hot spring
			if boolean_attribute_text == "Hot springs":
				trail_common_details.append(1)
			else:
				trail_common_details.append(0)

			#cave
			if boolean_attribute_text == "Cave":
				trail_common_details.append(1)
			else:
				trail_common_details.append(0)

			#is Jamie? (psh, no)
			trail_common_details.append(0)

		##### getting trail details unique to each month and merging with commons data

		jan, feb, mar, may, jun, jul, aug, sep, oct, nov, dec = [], [], [], [], [], [], [], [], [], [], [], []
		show_more_reviews_btn = driver.find_element_by_xpath('//*[@id="reviews"]/div[3]/button')
		page_results = driver.find_element_by_xpath('//*[@id="stick-bar-parent"]/div[2]/div[2]/div').getText().split(" ")
		reviews_total_num = page_results[6]
		reviews_on_screen = page_results[4]

		while reviews_on_screen != reviews_total_num:
			show_more_reviews_btn.click()
			# time.sleep(1)
			reviews_on_screen = driver.find_element_by_xpath('//*[@id="stick-bar-parent"]/div[2]/div[2]/div').getText().split(" ").page_results[4]

		for i in range(reviews_total_num):
			month = driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[2]').getText.split(" ")[0]

			if month == "January" :
				jan.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "February":
				feb.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "March":
				mar.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "April":
				apr.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "May":
				may.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "June":
				june.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "July":
				july.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "August":
				aug.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "September":
				sep.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "October":
				oct.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "November":
				nov.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])
			elif month == "December":
				dec.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[' + str(i) + ']/div[1]/div[2]/span[1]').get_attribute("aria-label").split(" ")[0])

		if jan.length > 0:
			trail_data.append(trail_common_details.insert(3, "January").append(sum(jan)/jan.length))

		if feb.length > 0:
			trail_data.append(trail_common_details.insert(3, "February").append(sum(feb)/feb.length))

		if mar.length > 0:
			trail_data.append(trail_common_details.insert(3, "March").append(sum(mar)/mar.length))

		if apr.length > 0:
			trail_data.append(trail_common_details.insert(3, "April").append(sum(apr)/apr.length))

		if may.length > 0:
			trail_data.append(trail_common_details.insert(3, "May").append(sum(may)/may.length))

		if jun.length > 0:
			trail_data.append(trail_common_details.insert(3, "June").append(sum(jun)/jun.length))

		if jul.length > 0:
			trail_data.append(trail_common_details.insert(3, "July").append(sum(jul)/jul.length))

		if aug.length > 0:
			trail_data.append(trail_common_details.insert(3, "August").append(sum(aug)/aug.length))

		if sep.length > 0:
			trail_data.append(trail_common_details.insert(3, "September").append(sum(sep)/sep.length))

		if oct.length > 0:
			trail_data.append(trail_common_details.insert(3, "October").append(sum(oct)/oct.length))

		if nov.length > 0:
			trail_data.append(trail_common_details.insert(3, "September").append(sum(nov)/nov.length))

		if dec.length > 0:
			trail_data.append(trail_common_details.insert(3, "December").append(sum(dec)/dec.length))

	np.savetxt("alltrails_data.csv", trail_data, delimiter = ",")


scrape_trails(driver, getTrailUrls(driver, master_url))








































