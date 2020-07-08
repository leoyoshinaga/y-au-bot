from selenium import webdriver
from secrets import store
from utils import *
import time

#rewrite parse_time using datetime



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

  # return if the highest bid is greater than max bid here
  minimum_bid = driver.find_element_by_id('nextBid').text
  print(yen_to_int(minimum_bid))
  # value = Decimal(sub(r'[^\d.]', '', highest_bid.get_attribute('data-usd')))

  if yen_to_int(minimum_bid) > store['maxbid']:
    print('Your max bid is lower than the minimum bid. Cannot Bid.')



  #find remaining time and evaluate it
  time_left = driver.find_element_by_xpath('//*[@id="lblTimeLeft"]')
  print(parse_time(time_left.text))
  time.sleep(parse_time(time_left.text) - 200)
  driver.refresh()

  while minimum_bid < store['maxbid']:
    driver.find_element_by_xpath('//*[@id="make_bid_logged"]').click()

  """
  if its greater than an hour sleep until the auction is 5 mins away
  while the price is less than the maxbid :

    time.sleep(240)
    driver.refresh()
  """
