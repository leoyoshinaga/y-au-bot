from selenium import webdriver
from secrets import store
import time



if __name__ == '__main__':
  #open chrome
  driver = webdriver.Chrome('./chromedriver')
  #goes to url
  driver.get(store['url'])
  #close pop up
  time.sleep(1)
  driver.find_element_by_xpath('//*[@id="signUpOfferWindow"]/div/div/div[1]/button').click()
  #sign in
  driver.find_element_by_xpath('//*[@id="header1_not_logged_menu"]/a[1]').click()
  driver.find_element_by_xpath('//*[@id="tbxLogin"]').send_keys(store['email'])

  # driver.find_element_by_xpath('').send_keys()
  # while True:
  #   time.sleep()

