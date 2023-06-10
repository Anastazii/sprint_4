from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_FIRST_QUESTION = (By.ID, "accordion__heading-0") #первый вопрос
    LOCATOR_SECOND_QUESTION = (By.ID, "accordion__heading-1") #второй вопрос
    LOCATOR_THIRD_QUESTION = (By.ID, "accordion__heading-2") #третий вопрос
    LOCATOR_FOURTH_QUESTION = (By.ID, "accordion__heading-3") #4 вопрос
    LOCATOR_FIFTH_QUESTION = (By.ID, "accordion__heading-4") #5 вопрос
    LOCATOR_SIXTH_QUESTION = (By.ID, "accordion__heading-5") #6 вопрос
    LOCATOR_SEVENTH_QUESTION = (By.ID, "accordion__heading-6") #7 вопрос
    LOCATOR_EIGHTH_QUESTION = (By.ID, "accordion__heading-7") #8 вопрос
    LOCATOR_COOKIE_BUTTON = (By.ID, "rcc-confirm-button") #кнопка куки
    LOCATOR_TOP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")  # Кнопка заказа(верхняя)
    LOCATOR_LOW_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка заказа(нижняя)
    LOCATOR_NAME = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле для ввода имени
    LOCATOR_LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле для ввода фамилии
    LOCATOR_ADDRESS_FORM = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле для ввода адреса
    LOCATOR_METRO_STATION = (By.CLASS_NAME, "select-search__input")  # Кнопка метро
    LOCATOR_STATION_SELECTION = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[3]/button")  # Выбор станции метро
    LOCATOR_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле для ввода телефона
    LOCATOR_FURTHER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка продолжить
    LOCATOR_DATE_ENTRY_FIELD = (By.XPATH, "//div[@class='react-datepicker__input-container']//input[@type='text']")  # Поле для ввода даты
    LOCATOR_DATE_CONFIRMATION = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS " "div.Order_Form__17u6u div.Order_MixedDatePicker__3qiay " "div.react-datepicker__tab-loop div.react-datepicker-popper " "div.react-datepicker " "div.react-datepicker__month-container:nth-child(4) " "div.react-datepicker__month " "div.react-datepicker__week:nth-child(3) > " "div.react-datepicker__day.react-datepicker__day--018.react" "-datepicker__day--weekend:nth-child(7)") # Подтверждение даты
    LOCATOR_RENTAL_PERIOD_BUTTON = (By.XPATH, "//div[@class='Dropdown-control']")  # Кнопка выбора периода времени катания
    LOCATOR_RENTAL_PERIOD_CHOICE = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(3)")  # Выбираем период времени
    LOCATOR_COLOR_SCOOTER = (By.CLASS_NAME, "Checkbox_Input__14A2w")  # Выбираем цвет самоката
    LOCATOR_COMMENTARY = (By.XPATH, "//div[@class='Order_Form__17u6u']//div[""@class='Input_InputContainer__3NykH']//input[@type='text']") # Поле для ввода комментария
    LOCATOR_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка заказать, перед подтверждением заказа
    LOCATOR_CONFIRM_BUTTON = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Modal__YZ-d3 " "div.Order_Buttons__1xGrp > " "button.Button_Button__ra12g.Button_Middle__1CSJM:nth-child(2)")  # Кнопка Да
    LOCATOR_VIEW_STATUS = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                            "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                            "button.Button_Button__ra12g.Button_Middle__1CSJM") #Кнопка проверить статус
    LOCATOR_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR") #кнопка Самокат
    LOCATOR_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI") #кнопка Яндекс
