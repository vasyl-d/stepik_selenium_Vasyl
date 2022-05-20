from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    selector = ["[id='input_value']",
        "[id='answer']",
        "[id='robotCheckbox']",
        "[id='robotsRule']"]

    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector(selector[0]).text
    y = calc(x)

    answer = browser.find_element_by_css_selector(selector[1])
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(str(y))

    for i in [2,3]:
        browser.find_element_by_css_selector(selector[i]).click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()