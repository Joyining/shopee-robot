# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, time
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get('https://rhinoshield.tw/collections/designers-toy-story?device=iphone-14&type=clear-case&prod=iphone-14-clear-case-pa79&bcolor=crystal_clear&ctype=clear-case-magsafe&page=0&limit=12&dcolor=MorningMist')

try:
  cookie_ok = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.cookie-policy__wrap__switcher button'))
  )
  cookie_ok.click()
except:
  print('cookie ok failed.')

try:
  cross_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="caseProduct"]/div[3]/div/div[2]/div[3]/div/div[1]/button'))
  )
  cross_button.click()
except:
  cookie_ok = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.cookie-policy__wrap__switcher button'))
  )
  cookie_ok.click()
  cross_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="caseProduct"]/div[3]/div/div[2]/div[3]/div/div[1]/button'))
  )
  cross_button.click()

try:
  black_cross = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cosmos_black"]/div/input'))
  )
  black_cross.click()
except:
  cookie_ok = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.cookie-policy__wrap__switcher button'))
  )
  cookie_ok.click()
  black_cross = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cosmos_black"]/div/input'))
  )
  black_cross.click()

try:
  add_to_card_0 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="caseProduct"]/div[3]/div/div[6]/button'))
  )
  add_to_card_0.click()
except:
  cookie_ok = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.cookie-policy__wrap__switcher button'))
  )
  cookie_ok.click()
  add_to_card_0 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="caseProduct"]/div[3]/div/div[6]/button'))
  )
  add_to_card_0.click()

sticker = WebDriverWait(driver, 10).until(
  EC.element_to_be_clickable((By.XPATH, '//*[@id="add__on"]/div[3]/div/ul[1]/li[2]/label'))
)
sticker.click()

add_to_card_1 = driver.find_element(By.XPATH, '//*[@id="add__on"]/div[3]/button')
add_to_card_1.click()

select_shipment = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.XPATH, '//*[@id="shipping"]/select'))
)
Select(select_shipment).select_by_visible_text('黑貓寄送')

promo_code = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.XPATH, '//*[@id="storePickupApp"]/div[1]/div[1]/div[1]/div[3]/div/input'))
)
apply = driver.find_element(By.XPATH, '//*[@id="storePickupApp"]/div[1]/div[1]/div[1]/div[3]/div/button')

startTime = time(*(map(int, '12:00'.split(':'))))
print(startTime)
print(datetime.today().time())

attempts = 0
while attempts < 10:
  try:
    promo_code.send_keys('')
    # promo_code.send_keys('one1111')
    promo_code.send_keys('ya1111-rs')
    while startTime > datetime.today().time():
      print('sleep')
      sleep(1)
    apply.click()

    discount_tag = WebDriverWait(driver, 1).until(
      EC.presence_of_element_located((By.CLASS_NAME, 'discount__tag'))
    )
    break
  except:
    attempts += 1
    print('promo code error')

if (attempts < 10):
  try:
    check_link = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))
    )
    check_link.click()
  except:
    cookie_ok = WebDriverWait(driver, 20).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR, '.cookie-policy__wrap__switcher button'))
    )
    cookie_ok.click()
    check_link = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))
    )
    check_link.click()

  email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_email"]'))
  )
  email.send_keys('anny60930@hotmail.com')

  family_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_shipping_address_first_name"]'))
  )
  family_name.send_keys('劉')

  first_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_shipping_address_last_name"]'))
  )
  first_name.send_keys('建榮')

  address = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_shipping_address_address1"]'))
  )
  address.send_keys('北屯區新興路3號3樓')

  select_shipment = Select(driver.find_element(By.XPATH, '//*[@id="checkout_address_city_selector"]'))
  select_shipment.select_by_visible_text('台中市')

  postal_code = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_shipping_address_zip"]'))
  )
  postal_code.send_keys('40645')

  phone = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_shipping_address_phone"]'))
  )
  phone.send_keys('0926600680')

  continue_button_0 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="continue_button"]'))
  )
  continue_button_0.click()

  continue_button_1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="continue_button"]'))
  )
  continue_button_1.click()

  payment = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_payment_gateway_60536901"]'))
  )
  payment.click()

  confirm = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="continue_button"]'))
  )
  confirm.click()


