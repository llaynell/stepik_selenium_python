from selenium import webdriver
import time

url = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(url)

# Обязательные поля
input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
input1.send_keys("Lay")

input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
input2.send_keys("mail@inbox.com")

# Отправка
button = browser.find_element_by_css_selector("button.btn")
button.click()


# Проверка успешной регистрации
# ждать загрузку страницы
time.sleep(1)

# элемент с текстом
welcome_text_elt = browser.find_element_by_tag_name("h1")
# сам текст
welcome_text = welcome_text_elt.text

# проверка текста, мы зарегистрировались
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text