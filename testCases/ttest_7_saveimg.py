from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from testCases import GenerateXpath
from utilities.customLogger import LogGen
from selenium.webdriver.common.action_chains import ActionChains
from testCases import wait_click
import time
import testCases.test_1_home as br_st
import testCases.variables as vr
import os.path
import datetime
import glob

# baseURL = "http://127.0.0.1/monitor"
menuitem_xpath = "(//*[@role='menuitem'])"
logger = LogGen.loggen()
play_button_xpath = "//*[@aria-label = 'Play/Pause']"
stop_button_xpath = "//*[@aria-label = 'Play/Pause']"
save_image_button_xpath = "//*[@aria-label = 'Save']"
options_button_xpath = "//*[@aria-label = 'Options']"
menu_button_xpath = "//mat-icon[contains(text(),'menu')]"
monitor_item_xpath = "//*[normalize-space()='desktop_windows']"  # //*[normalize-space()='Monitor']
high_radio_xpath = "//*[@value='high']"
medium_radio_xpath = "//*[@value='medium']"
low_radio_xpath = "//*[@value='low']"
all_radio_xpath = "//*[@value='all']"
pos_radio_xpath = "//*[@value='positives']"
nega_radio_xpath = "//*[@value='negatives']"
show_code_list_xpath = "//*[contains(text(),'Show Code List')]"
show_web_monitor_xpath = "//*[contains(text(),'Show Web Monitor')]"
show_coor = "//*[contains(text(),'Show Coordinates')]"
image_sc_box_xpath = "//*[contains(text(),'Images/Second:')]"
coor_box_xpath = "//*[contains(text(),'X:')]"
flag = True
time_out = 10
time_out_5 = 5
mode = 0  # mode =1: goodread, mode =2: phasemode, mode =3 no goodread


def monitor_button(driver):
    global mode, flag
    logger.info("**********Verify Monitor button!***************\n")
    try:
        driver.find_element_by_xpath(menu_button_xpath).click()
        wait_click.click_until_interactable(driver.find_element_by_xpath(monitor_item_xpath))
    except Exception:
        flag = False
        logger.error("Error Click - Monitor")

    # options.add_experimental_option("prefs", {
    #     "download.default_directory": r"C:\Users\24H\Downloads\img",
    #     "download.prompt_for_download": False,
    #     "download.directory_upgrade": True,
    #     "safebrowsing.enabled": True
    # })

    logger.info("**********Verify Save image button!***************\n")
    time.sleep(2)
    try:
        driver.find_element_by_xpath(save_image_button_xpath).click()
        d_time = datetime.datetime.now()
        d_time = d_time.strftime("%a %b %d %Y")
        file_name = "image_" + d_time + ".jpg"
        file_path = "C:\\Users\\24H\\Downloads\\img\\" + file_name
        while not os.path.exists(file_path):
            time.sleep(0.5)
        # check file
        if os.path.isfile(file_path):
            logger.info("**********File download is completed!***************\n")
            logger.info("**********Save image button test is passed!***************\n")
        else:
            logger.info("**********File download is not completed!***************\n")
            logger.error("**********Save image button test is worked!***************\n")
        time.sleep(3)
        list_of_files = glob.glob("C:\\Users\\24H\\PycharmProjects\\pytest_web\\Download\\*.jpg")
        latest_file = max(list_of_files, key=os.path.getmtime)
        print(latest_file)
        modTimesinceEpoc = os.path.getmtime(latest_file)
        modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
        print("Last Modified Time : ", modificationTime)
    except Exception:
        flag = False
        logger.error("Save image button is not worked")


def test_monitorpage(browser):
    global flag
    if vr.driver is None:
        br_st.browser_setup(browser)
    logger.info("**********Test_002_MonitorPage***************\n")
    monitor_button(vr.driver)
    if flag == False:
        assert False
    # vr.driver.quit()
