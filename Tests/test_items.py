from selenium.webdriver.common.by import By
import time


def test_to_basket_button(browser):

    #открытие сайта
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    #поиск кнопки
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')

    #таймер для ручной проверки языка сайта
    #time.sleep(30)

    #проверка на ошибку
    assert button != [], print('"Add to basket" button not found')

    #вывод текста кнопки для проверки выбранного языка
    print(f'Add to basket button is called "{button[0].text}"')

