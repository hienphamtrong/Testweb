from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time


def is_time_out(start_time_millis: int, waiting_interval_seconds: int) -> bool:
    end_time = start_time_millis + waiting_interval_seconds * 1000
    return get_current_time_in_millis() > end_time


def get_current_time_in_millis() -> int:
    return int(time.time() * 1000)


def click_until_interactable(element: WebElement) -> bool:
    element_is_interactable = False
    start_time = get_current_time_in_millis()
    counter = 1
    if element:
        while not element_is_interactable and not is_time_out(start_time, 10):
            try:
                element.click()
                element_is_interactable = True
            except (ElementClickInterceptedException, ElementNotInteractableException) as e:
                counter = counter + 1
    # print("We've tried " + str(counter) + " times")
    return element_is_interactable


def wait_data_change(element: WebElement, current_data: str) -> bool:
    data_change = False
    start_time = get_current_time_in_millis()
    counter = 1
    try:
        while not is_time_out(start_time, 10):

            read_data = element.text
            if read_data != current_data:
                data_change = True
                break
            else:
                counter = counter + 1
        time.sleep(0.1)
    except Exception:
        if is_time_out(start_time,10):
            print("Time out-Data not change")
    # print("We've tried: " + str(counter) + " times")
    return data_change


def is_green(element: WebElement) -> bool:
    element_is_green = False
    start_time = get_current_time_in_millis()
    counter = 1
    try:
        while not is_time_out(start_time, 10):

            if "material-icons selected-icon" in element.get_attribute('class'):
                element_is_green = True
                break
            else:
                counter = counter + 1
            time.sleep(0.1)
    except Exception:
        if is_time_out(start_time, 10):
            print("Time out-Data not change")

    # print("We've tried " + str(counter) + " times")
    return element_is_green


def click_any_where(driver, times: int):
    actions = ActionChains(driver)
    if times == 1:
        actions.move_by_offset(400, 400).click().perform()
    else:
        actions.move_by_offset(0, 0).click().perform()

