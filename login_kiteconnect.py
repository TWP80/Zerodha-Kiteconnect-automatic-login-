"""
  Created by Deepak yadav on 19 Feb 2018
  
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urlparse import urlparse, parse_qs

#for logging into firefox browser, user can use other browser like chrome by appropriately adding corresponding webdriver
driver = webdriver.Firefox()

#Always a constant for unique user_id and can be found by logging in kiteconnect. Paste the redirect-url below at time of logging
#into kiteconnect. It's a one time activity.

driver.get("https://kite.trade/connect/login?api_key=xxxxxyyyyyyzzzz111222333")

#Dictionary for set of secret questions can be found out by 2-3 times login into zerodha account and create your own dictionary 
#for logging in. An example is shown below, your answers goes in marked by 'xxxxxx'
dictionary={
        'Which brand of TV do you own? ( e.g. LG Sony, etc)': 'xxxxxx',
        'Which year did you complete your graduation? (e.g. 2000, 1990 etc)': 'xxxxx',
        'What\'s the most famous landmark near your home? (e.g. Xyz Theater, XXX Mall, etc)':'xxxxx',
        'What was the make of the first computer you owned? ( e.g. LG, Compaq etc)':'xxxxxx',
        'What is your birth place?':'xxxxx'      
        }

# write your User Id
loginid = "AB1234"
# write your Password
password = "abc@123"
# write your PIN
loginpin = "123456"

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"userid"))).send_keys(loginid)
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"password"))).send_keys(password)


driver.find_element_by_name('login').click()

driver.implicitly_wait(10)



''' Get answer to question 1'''
input1=dictionary[driver.find_element_by_class_name("first").text]
answer1=driver.find_element_by_name("answer1")
answer1.send_keys(input1)

''' Get answer to question 2'''
input2=dictionary[driver.find_element_by_class_name("second").text]
answer2=driver.find_element_by_name("answer2")
answer2.send_keys(input2)


driver.find_element_by_name('twofa').click()

url=driver.current_url
parse_url = urlparse(url)
query = parse_qs(parse_url.query)
request_token=query['request_token']

api_key="Your api_key"
api_secret="Your api_secret"
kite=KiteConnect(api_key=api_key)

data = kite.generate_session(request_token[0], api_secret)

kws = KiteTicker("Your api_key" ,data["access_token"], "Your user_id")
