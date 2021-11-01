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
import glob
import datetime

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


def opt_button_monitor(driver):
    global flag
    logger.info("**********Verify radio button!***************\n")
    try:
        # WebDriverWait(driver, time_out).until(EC.element_to_be_clickable((By.XPATH, medium_radio_xpath)))
        check = driver.find_element_by_xpath(high_radio_xpath).get_attribute('class')
        time.sleep(0.5)
        if "checked" in check:
            driver.find_element_by_xpath(medium_radio_xpath).click()
            driver.find_element_by_xpath(low_radio_xpath).click()
            driver.find_element_by_xpath(high_radio_xpath).click()
        else:
            driver.find_element_by_xpath(high_radio_xpath).click()
            driver.find_element_by_xpath(medium_radio_xpath).click()
            driver.find_element_by_xpath(low_radio_xpath).click()
    except Exception:
        flag = False
        logger.error("Image Quality radio button is not worked")
    try:
        check = driver.find_element_by_xpath(all_radio_xpath).get_attribute('class')

        if "checked" in check:
            driver.find_element_by_xpath(pos_radio_xpath).click()
            driver.find_element_by_xpath(nega_radio_xpath).click()
            driver.find_element_by_xpath(all_radio_xpath).click()
        else:
            driver.find_element_by_xpath(all_radio_xpath).click()
            driver.find_element_by_xpath(pos_radio_xpath).click()
            driver.find_element_by_xpath(nega_radio_xpath).click()
    except Exception:
        flag = False
        logger.error("Image Options radio button is not worked")
    logger.info("**********Radio button test is completed!***************\n")


def view_pt_monitor(driver):
    global flag, check_loop

    logger.info("**********Verify slide toggle!***************\n")
    try:
        driver.find_element_by_xpath(show_web_monitor_xpath).click()
        logger.info("Show Web Monitor is ON")
        WebDriverWait(driver, time_out).until(EC.visibility_of_element_located((By.XPATH, image_sc_box_xpath)))
        logger.info("Images/Second box - Expected: visibility - Actual: visibility")
    except Exception:
        flag = False
        logger.error("Images/Second box - Expected: visibility - Actual: invisibility")

    try:
        driver.find_element_by_xpath(show_coor).click()
        logger.info("Show Coordinates is ON")
        WebDriverWait(driver, time_out).until(EC.visibility_of_element_located((By.XPATH, coor_box_xpath)))
        logger.info("Coordinates box - Expected: visibility - Actual: visibility")
    except Exception:
        flag = False
        logger.error("Coordinates box - Expected: visibility - Actual: invisibility")
    try:
        driver.find_element_by_xpath(show_code_list_xpath).click()
        logger.info("Show Code List is ON")
    except Exception:
        flag = False

    # click anywhere
    try:
        wait_click.click_any_where(driver,2)

    except Exception:
        pass

    if mode == 1:
        try:
            xpath_code99 = "//*[contains(text(),'#99 ')]"
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath_code99)))
            driver.find_element_by_xpath(stop_button_xpath).click()
            code_1 = GenerateXpath.generate_xpath(driver.find_element_by_xpath("//*[contains(text(),'#1 ')]"), "")
            code_99 = GenerateXpath.generate_xpath(driver.find_element_by_xpath("//*[contains(text(),'#99 ')]"), "")

            for i in range(0, len(code_99)):
                if code_99[i] != code_1[i] and int(code_99[i]) - int(code_1[i]) == 1:
                    check_loop = True
                    break

            if check_loop:
                logger.info("Show Code List - Expected: visibility - Actual: visibility")
                logger.info("**********The cycle of code list is 99!**********")
            else:
                flag = False
                logger.info("Show Code List - Expected: visibility - Actual: visibility")
                logger.error("**********The cycle of code list is not 99!**********")
        except Exception:
            logger.error("**********Show Code List is not worked!**********")
    else:
        try:
            WebDriverWait(driver, time_out).until(
                EC.invisibility_of_element_located((By.XPATH, "//*[contains(text(),'#1 ')]")))
            logger.info("Show Code List - Expected: invisibility - Actual: invisibility")
        except Exception:
            flag = False
            logger.error("Show Code List - Expected: invisibility - Actual: visibility")

    try:
        driver.find_element_by_xpath(options_button_xpath).click()
        WebDriverWait(driver, time_out).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'mat-drawer-shown')]")))
        wait_click.click_until_interactable(driver.find_element_by_xpath(show_code_list_xpath))
        logger.info("Show Code List is OFF")

        driver.find_element_by_xpath(show_web_monitor_xpath).click()
        logger.info("Show Web Monitor is OFF")
        WebDriverWait(driver, time_out).until(EC.invisibility_of_element_located((By.XPATH, image_sc_box_xpath)))
        driver.find_element_by_xpath("//*[contains(text(),'Show Coordinates')]").click()

        logger.info("Show Coordinates is OFF")
        WebDriverWait(driver, time_out).until(EC.invisibility_of_element_located((By.XPATH, coor_box_xpath)))
        try:
            wait_click.click_any_where(driver, 2)
        except Exception:
            pass

    except Exception:
        flag = False
        logger.error("Error when turn OFF slide toggle")
    logger.info("**********Slide toggle test is completed!***************\n")


def monitor_button(driver):
    global mode, flag
    logger.info("**********Verify Monitor button!***************\n")
    try:
        driver.find_element_by_xpath(menu_button_xpath).click()
        wait_click.click_until_interactable(driver.find_element_by_xpath(monitor_item_xpath))
    except Exception:
        flag = False
        logger.error("Error Click - Monitor")

    try:
        if WebDriverWait(driver, time_out_5).until(EC.presence_of_element_located((By.XPATH, "//*[@fill = 'green']"))):
            mode = 1
            logger.info("Mode: Have Image - Good Read")
    except Exception:
        try:
            if WebDriverWait(driver, time_out_5).until(EC.presence_of_element_located((By.XPATH, "//*[@disabled]"))):
                mode = 2
                logger.info("Mode: No Image")
        except Exception:
            mode = 3
            logger.info("Mode: Have Image - No Read")
            pass

    print(mode)
    try:
        driver.find_element_by_xpath(stop_button_xpath).click()
        driver.find_element_by_xpath(play_button_xpath).click()
    except Exception:
        flag = False
        logger.error("Play/Pause button is not worked!")

    logger.info("**********Verify Save image button!***************\n")
    if mode != 2:
        try:
            driver.find_element_by_xpath(save_image_button_xpath).click()
            # d_time = datetime.datetime.now()
            # d_time = d_time.strftime("%a %b %d %Y")
            # file_name = "image_" + d_time + ".jpg"
            # file_path = "C:\\Users\\24H\\Downloads\\" + file_name
            # while not os.path.exists(file_path):
            #     time.sleep(0.5)
            # # check file
            # if os.path.isfile(file_path):
            #     logger.info("**********File download is completed!***************\n")
            #     logger.info("**********Save image button test is passed!***************\n")
            # else:
            #     logger.info("**********File download is not completed!***************\n")
            #     logger.error("**********Save image button test is worked!***************\n")
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
    else:
        logger.info("Save image button is disable\n")

    try:
        driver.find_element_by_xpath(options_button_xpath).click()
        WebDriverWait(driver, time_out_5).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'mat-drawer-shown')]")))
    except Exception:
        try:
            driver.find_element_by_xpath(options_button_xpath).click()
            WebDriverWait(driver, time_out_5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'mat-drawer-shown')]")))
        except Exception:
            flag = False
            logger.error("Options button is not worked")
    logger.info("**********Monitor button test is completed!***************\n")


def test_monitorpage(browser):
    global flag
    if vr.driver is None:
        br_st.browser_setup(browser)
    logger.info("**********Test_002_MonitorPage***************\n")
    monitor_button(vr.driver)
    opt_button_monitor(vr.driver)
    view_pt_monitor(vr.driver)
    if flag == False:
        assert False
    # vr.driver.quit()
