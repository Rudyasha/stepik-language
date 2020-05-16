import time
from selenium import chromedriver
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket():
  browser.get(link)
  time.sleep(30)
  basket = browser.find_element_by_xpath(//button[@class='btn btn-lg btn-primary btn-add-to-basket'])
  
  assert len(basket) > 0
