from selenium import webdriver
from secrets import store
import time

def parse_time(time_str):
  i = 0
  length = len(time_str)
  while i < length:
    char = time_str[i]
    if str.isdigit(char):
      return
    if char == 'h' or char == 'm':
      return float('inf')
    i+=1
  return


if __name__ == '__main__':
  #open chrome
  driver = webdriver.Chrome('./chromedriver')
  #goes to url
  driver.get(store['url'])
  #close pop up
  time.sleep(3)
  driver.find_element_by_xpath('//*[@id="signUpOfferWindow"]/div/div/div[1]/button').click()
  #sign in
  driver.find_element_by_xpath('//*[@id="header1_not_logged_menu"]/a[1]').click()
  driver.find_element_by_xpath('//*[@id="tbxLogin"]').send_keys(store['email'])
  driver.find_element_by_xpath('//*[@id="tbxPassword"]').send_keys(store['pw'])
  driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
  time.sleep(5)
  #find remaining time and evaluate it
  x = driver.find_element_by_xpath('//*[@id="lblTimeLeft"]')
  parse_time(x.text)
  """
  while True:

    time.sleep(240)
    driver.refresh()
  """
