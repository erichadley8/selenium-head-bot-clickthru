from selenium import webdriver
import random


while True:

	driver = webdriver.Firefox()
	driver.get('http://www.porngifs.xyz/')

	driver.switch_to.window(driver.window_handles[1])
	driver.close()

	driver.switch_to.window(driver.window_handles[0])

	elements = driver.find_elements_by_class_name("card-img-top")
	
	clickthrough = random.choice(elements)

	clickthrough.click()
	driver.switch_to.window(driver.window_handles[1])
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	driver.close()
	
