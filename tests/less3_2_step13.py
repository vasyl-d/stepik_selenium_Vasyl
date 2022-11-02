from selenium import webdriver
import time
import unittest


class TestLink(unittest.TestCase):
    self.wel_mess = "Congratulations! You have successfully registered!"

    def op_link(link):
        welcome_text = ''
        try:
            value = ['.first_block > .form-group > .first',
                     '.first_block > .form-group > .second',
                     '.first_block > .form-group > .third']

            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            for vl in value:
                element = browser.find_element_by_css_selector(vl)
                element.send_keys("Ответ")

            # Отправляем заполненную форму
            browser.find_element_by_css_selector("button.btn").click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text = browser.find_element_by_tag_name("h1").text
            # записываем в переменную welcome_text текст из элемента welcome_text_elt

        except Exception as ex:
            welcome_text = f"An exception of type {type(ex).__name__} occurred."

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
        return welcome_text

    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        mess = self.op_link(link)
        self.assertEqual(mess, self.wel_mess, mess)

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        mess = self.op_link(link)
        self.assertEqual(mess, self.wel_mess, mess)



if __name__ == "__main__":
    unittest.main()