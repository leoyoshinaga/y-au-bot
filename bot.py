from selenium import webdriver
import time

store = {
  'url': 'https://zenmarket.jp/en/auction.aspx?itemCode=e447723398'
  # maxBid:
}


if __name__ == '__main__':
  driver = webdriver.Chrome('./chromedriver')
  driver.get(store['url'])
  # while True:

  #   time.sleep()

