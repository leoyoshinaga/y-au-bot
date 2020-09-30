from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from secrets import store
from utils import *
import time

def get_remaining_secs():
  return parse_time(driver.find_element_by_id('lblTimeLeft').text)

def place_bid():
  driver.find_element_by_id('make_bid_logged').click()
  time.sleep(5)
  driver.find_element_by_id('makeBidModal').click()
  time.sleep(1)
  driver.find_element_by_id('YahooBidModal_cbxCondition1').click()
  driver.find_element_by_id('YahooBidModal_cbxCondition2').click()
  driver.find_element_by_id('YahooBidModal_cbxCondition3').click()
  driver.find_element_by_id('agreeButton').click()
  time.sleep(10)
  driver.refresh()
  time.sleep(10)

def snipe():
  while get_remaining_secs() > store['snipe_second'] + 10:
    print('Sleeping for half the time' + str(get_remaining_secs()/2) + 'seconds')
    time.sleep((get_remaining_secs() - store['snipe_second'])/2)
    driver.refresh()
    time.sleep(10)
  minimum_bid = yen_to_int(driver.find_element_by_id('nextBid').text)
  if minimum_bid > store['maxbid']:
    print('max bid too low')
    return
  print('done sleeping, now bidding')
  try:
    if driver.find_element_by_id('lblUserBid').text == driver.find_element_by_id('lblPriceY').text:
      print('already top bidder, camping again')
      return
    else:
      place_bid()
  except NoSuchElementException:
    place_bid()

if __name__ == '__main__':
  print('settings:', store)
  #open chrome
  driver = webdriver.Chrome('./chromedriver')
  #goes to url
  driver.get(store['url'])
  #close pop up
  time.sleep(10)
  driver.find_element_by_xpath('//*[@id="signUpOfferWindow"]/div/div/div[1]/button').click()
  #sign in
  driver.find_element_by_xpath('//*[@id="header1_not_logged_menu"]/a[1]').click()
  driver.find_element_by_id('tbxLogin').send_keys(store['email'])
  driver.find_element_by_id('tbxPassword').send_keys(store['pw'])
  driver.find_element_by_id('btnLogin').click()
  time.sleep(5)

  # return if the highest bid is greater than max bid here
  minimum_bid = yen_to_int(driver.find_element_by_id('nextBid').text)
  print(minimum_bid, store['maxbid'])
  # value = Decimal(sub(r'[^\d.]', '', highest_bid.get_attribute('data-usd')))

  if minimum_bid > store['maxbid']:
    print('Your max bid is lower than the minimum bid. Cannot Bid.')
  else:
    print('Proceeding to camping and sleeping. Standing By.')



  #find remaining time and evaluate it
  time_left = get_remaining_secs()
  #if theres more than a day, sleep for the days first
  days = time_left - time_left % 86400
  if days > 86400:
    print('sleeping till the last day')
    time.sleep(days)
    driver.refresh()
    time.sleep(10)

  #camp and snipe
  snipe()

  while yen_to_int(driver.find_element_by_id('nextBid').text) < store['maxbid']:
    if driver.find_element_by_id('lblUserBid').text != driver.find_element_by_id('lblPriceY').text:
      snipe()
    driver.refresh()
    time.sleep(10)


print('bot finished')
