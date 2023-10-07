from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoAlertPresentException,UnexpectedAlertPresentException,NoSuchElementException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import openpyxl

#------------------------------------
total_gata=range(1,600)
urad_gata=[]
rikt_fasal=[]
blank_gata=[]



serv_obj=Service("chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

PASSWORD = "password"
DISTRICT_VALUE = "136"
TEHSHIL_VALUE = "00727"
HALKA_VALUE = "0113600727037"
FASAL_NAME_VALUE = "3" #dhan
rikt_fasal_value="67" # rikt
SICAHAI_VIDHI = "3"
DHAN_FASAL_NAME_VALUE = "5"
ikh_boi_fasal_value="25"
ikh_pedi_fasal_value="26"
urad_fasal_value="18"

number_x_path_map = {
    "1": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[1]/a/div",
    "2": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[2]/a/div",
    "3": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[3]/a/div",
    "4": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[4]/a/div",
    "5": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[1]/a/div",
    "6": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[2]/a/div",
    "7": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[3]/a/div",
    "8": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[4]/a/div",
    "9": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[1]/a/div",
    "0": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[2]/a/div",
    "delete": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[3]/a/div",
    "clear": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[4]/a/div"
}

XPATH_MAPPING = {
    "SURAKSHIT_KAREIN_BUTTON": "//*[@id=\"tab-3\"]/form/p/table[3]/tbody/tr/td[1]/input[5]",
    "BACK_BUTTON_ON_SICHAI_PAGE": "//*[@id=\"content\"]/center/header/div/div[7]/div"
}


def load_first_page():
    driver.get("http://164.100.59.148/")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/center/main/div/div/ul/li[4]/a/div/div[1]").click()
    time.sleep(.25)


def load_second_page():
    selectDistrict = Select(driver.find_element(By.ID, "up_district"))
    selectDistrict.select_by_value(DISTRICT_VALUE)
    time.sleep(.5)
    selectTehsil = Select(driver.find_element(By.ID, "up_tehsil"))
    selectTehsil.select_by_value(TEHSHIL_VALUE)
    time.sleep(.5)
    selectTehsil = Select(driver.find_element(By.ID, "up_halka"))
    selectTehsil.select_by_value(HALKA_VALUE)
    time.sleep(.5)
    captcha_value = driver.find_element(By.ID, "CaptchaDiv").text
    driver.find_element(By.ID, "CaptchaInput").send_keys(captcha_value)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()


def load_third_page():
    time.sleep(20)


def load_fourth_page():
    time.sleep(10)
    # driver.find_element(By.XPATH, "//*[@id=\"link2\"]/a/div/div[2]").click()
    fill_form()


def fill_form():
    time.sleep(0.5)
    for i in total_gata:

        if i in rikt_fasal:
            rikt_privisti(i)
            print(i, "rikt")
            continue

        elif i in urad_gata:
            urad_privisti(i)
            print(i,"urad")
    
        elif i in blank_gata:
            print(i,"blank")
            continue
        
        else:
            dhan_privisti(i)
            print(i,"dhan")
            
            



def click_digits(digits):
    for digit in digits:
        driver.find_element(By.XPATH, number_x_path_map[digit]).click()


def search_number(number):
    click_digits(str(number))
    driver.find_element(By.XPATH, "//*[@id=\"sgw\"]/button/i").click()
    return get_min_gata_list()


def get_min_gata_list():
    try:
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
        search_gata = driver.find_element(By.CLASS_NAME, "search-data-list")
        search_gata_list = search_gata.find_elements(By.TAG_NAME, "li")
    except TimeoutException as e:
        search_gata_list = []
    return search_gata_list


def dhan_privisti(i):
    search_gata_list = search_number(i)
    if len(search_gata_list) == 0:
        driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
        time.sleep(3)
        return
    for gata_index in range(0, len(search_gata_list)):
        if gata_index != 0:
            driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
            current_gata_list = search_number(i)
        else:
            current_gata_list = search_gata_list

        gata_element = current_gata_list[gata_index]
        time.sleep(0.5)
        try:
            # WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
            # driver.find_element(By.NAME, "khata_number").click()
            # gata_element.click()
            gata_element.find_element(By.NAME, "khata_number").click()
            driver.find_element(By.XPATH, "//*[@id=\"case_frm\"]/button[2]").click()
            time.sleep(0.5)
            Select(driver.find_element(By.ID, "fasal_name")).select_by_value(DHAN_FASAL_NAME_VALUE)
            time.sleep(1)
            agri_area = driver.find_element(By.ID, "agriArea").get_attribute('value')
            if float(agri_area) >= 1.0:
                SICAHAI_VIDHI = "6"

            else:
                SICAHAI_VIDHI = "13"

            Select(driver.find_element(By.ID, "agriTech")).select_by_value(SICAHAI_VIDHI)
            driver.find_element(By.ID, "sichitArea").clear()
            driver.find_element(By.ID, "sichitArea").send_keys(agri_area)
            driver.find_element(By.XPATH, XPATH_MAPPING["SURAKSHIT_KAREIN_BUTTON"]).click()
            time.sleep(1)
            #driver.find_element(By.XPATH,number_x_path_map["BACK_BUTTON_ON_SICHAI_PAGE"]).click()
            driver.find_element(By.XPATH,"//*[@id=\"content\"]/center/header/div/div[7]/div").click()
        except Exception as e:
            # driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
            time.sleep(1)


def rikt_privisti(i):
    search_gata_list = search_number(i)
    if len(search_gata_list) == 0:
        driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
        time.sleep(3)
        return
    for gata_index in range(0, len(search_gata_list)):
        if gata_index != 0:
            driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
            current_gata_list = search_number(i)
        else:
            current_gata_list = search_gata_list

        gata_element = current_gata_list[gata_index]
        time.sleep(0.5)
        try:
            # WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
            # driver.find_element(By.NAME, "khata_number").click()
            # gata_element.click()
            gata_element.find_element(By.NAME, "khata_number").click()
            driver.find_element(By.XPATH, "//*[@id=\"case_frm\"]/button[2]").click()
            time.sleep(0.5)
            Select(driver.find_element(By.ID, "fasal_name")).select_by_value(rikt_fasal_value)
            time.sleep(1)
            # agri_area = driver.find_element(By.ID, "agriArea").get_attribute('value')
            # print(agri_area)
            # if float(agri_area) >= 1.0:
            #     SICAHAI_VIDHI = "6"
            #
            # else:
            #     SICAHAI_VIDHI = "13"
            #
            # Select(driver.find_element(By.ID, "agriTech")).select_by_value(SICAHAI_VIDHI)
            # driver.find_element(By.ID, "sichitArea").clear()
            # driver.find_element(By.ID, "sichitArea").send_keys(agri_area)
            driver.find_element(By.XPATH, XPATH_MAPPING["SURAKSHIT_KAREIN_BUTTON"]).click()
            time.sleep(1)
            #driver.find_element(By.XPATH,number_x_path_map["BACK_BUTTON_ON_SICHAI_PAGE"]).click()
            driver.find_element(By.XPATH,"//*[@id=\"content\"]/center/header/div/div[7]/div").click()
        except Exception as e:
            # driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
            time.sleep(1)


def urad_privisti(i):
    search_gata_list = search_number(i)
    if len(search_gata_list) == 0:
        driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
        time.sleep(3)
        return
    for gata_index in range(0, len(search_gata_list)):
        if gata_index != 0:
            driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
            current_gata_list = search_number(i)
        else:
            current_gata_list = search_gata_list

        gata_element = current_gata_list[gata_index]
        time.sleep(0.5)
        try:
            # WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
            # driver.find_element(By.NAME, "khata_number").click()
            # gata_element.click()
            gata_element.find_element(By.NAME, "khata_number").click()
            driver.find_element(By.XPATH, "//*[@id=\"case_frm\"]/button[2]").click()
            time.sleep(0.5)
            Select(driver.find_element(By.ID, "fasal_name")).select_by_value(urad_fasal_value)
            time.sleep(1)
            agri_area = driver.find_element(By.ID, "agriArea").get_attribute('value')
            #print(agri_area)
            if float(agri_area) >= 1.0:
                SICAHAI_VIDHI = "6"

            else:
                SICAHAI_VIDHI = "13"

            Select(driver.find_element(By.ID, "agriTech")).select_by_value(SICAHAI_VIDHI)
            driver.find_element(By.ID, "sichitArea").clear()
            driver.find_element(By.ID, "sichitArea").send_keys(agri_area)
            driver.find_element(By.XPATH, XPATH_MAPPING["SURAKSHIT_KAREIN_BUTTON"]).click()
            time.sleep(1)
            #driver.find_element(By.XPATH,number_x_path_map["BACK_BUTTON_ON_SICHAI_PAGE"]).click()
            driver.find_element(By.XPATH,"//*[@id=\"content\"]/center/header/div/div[7]/div").click()
        except Exception as e:
            # driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
            time.sleep(1)
















load_first_page()
load_second_page()
load_third_page()
load_fourth_page()







