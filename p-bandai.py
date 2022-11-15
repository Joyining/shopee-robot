# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 開啟瀏覽器視窗(Chrome)
driver = webdriver.Chrome('./chromedriver')
driver.get('https://p-bandai.com/tw/item/N2643494001001')

# popup_close = driver.find_element(By.CLASS_NAME, 'ab_widget_container_popin-image_close_button')
# popup_close.click()

recommended_close = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.CLASS_NAME, 'recommended-close'))
)
recommended_close.click()

cookie_close = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.CLASS_NAME, 'banner-close-button'))
)
cookie_close.click()



# select_size = Select(driver.find_element(By.ID, 'sc_p07_01_size'))
# select_size.select_by_visible_text('S')

# select_quantity = Select(driver.find_element(By.ID, 'sc_p07_01_purchaseNumber'))
# select_quantity.select_by_value('1')

submit_button = driver.find_element(By.ID, 'addToCartButton')
submit_button.click()

# submit_button = WebDriverWait(driver, 10).until(
#   EC.element_to_be_clickable((By.ID, 'addToCartButton'))
# )
# submit_button.click()

cart_link = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.XPATH, '//*[@id="addToCartLayer"]/div/div/div[2]/div[3]/a'))
)
cart_link.click()

confirm_link = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.XPATH, '//*[@id="o-content"]/div/main/section/section[1]/div/div[4]/div/div[1]/a'))
)
confirm_link.click()

user_name = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.ID, 'j_username'))
)
user_name.send_keys('yining1204@hotmail.com')

password = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.ID, 'j_password'))
)
password.send_keys('Wayne480107')

login_link = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/a'))
)
login_link.click()

credit_card = driver.find_element(By.XPATH, '//*[@id="pBOrderInfoForm"]/section[1]/div/div/section/div[3]/div/div[2]/div[1]/label')
credit_card.click()

invoice = driver.find_element(By.XPATH, '//*[@id="pBOrderInfoForm"]/section[1]/div/div/section/section[2]/div/div[1]/div[2]/div[1]/div/label[1]')
invoice.click()

return_check = driver.find_element(By.XPATH, '//*[@id="pBOrderInfoForm"]/section[1]/div/div/section/section[2]/div/div[1]/div[2]/div[2]/label')
return_check.click()

confirm_order = driver.find_element(By.XPATH, '//*[@id="confirmOrderInfo"]')
confirm_order.click()

agree = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.XPATH, '//*[@id="placeOrderForm"]/section[3]/div/label'))
)
agree.click()

pay = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.XPATH, '//*[@id="orderInfoConfirmBtn"]'))
)
pay.click()
