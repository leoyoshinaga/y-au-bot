from selenium import webdriver
from secrets import store
import time


def parse_time(time_str):
  #call time and end it at the end of the function
  seconds = 0
  i = 0
  length = len(time_str)
  num = ''
  while i < length:
    char = time_str[i]
    if str.isdigit(char):
      num += char
    elif char == 'd':
      intNum = int(num)
      seconds += intNum * 86400
      num = ''
    elif char == 'h':
      intNum = int(num)
      seconds += intNum * 3600
      num = ''
    elif char == 'm':
      intNum = int(num)
      seconds += intNum * 60
      num = ''
    elif char == 's':
      intNum = int(num)
      seconds += intNum
      num = ''
    i+=1
  return seconds



if __name__ == '__main__':
  #open chrome
  driver = webdriver.Chrome('./chromedriver')
  #goes to url
  driver.get(store['url'])
  #close pop up
  time.sleep(10)
  driver.find_element_by_xpath('//*[@id="signUpOfferWindow"]/div/div/div[1]/button').click()
  #sign in
  driver.find_element_by_xpath('//*[@id="header1_not_logged_menu"]/a[1]').click()
  driver.find_element_by_xpath('//*[@id="tbxLogin"]').send_keys(store['email'])
  driver.find_element_by_xpath('//*[@id="tbxPassword"]').send_keys(store['pw'])
  driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
  time.sleep(5)
  #find remaining time and evaluate it
  time_left = driver.find_element_by_xpath('//*[@id="lblTimeLeft"]')
  print(parse_time(time_left.text))
  """
  while True:
    if the price is greater than the maxbid break
    if its greater than an hour sleep for the amount of time
    time.sleep(240)
    driver.refresh()
  """
