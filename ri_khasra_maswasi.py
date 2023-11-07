from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoAlertPresentException, UnexpectedAlertPresentException, \
    NoSuchElementException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import openpyxl

PASSWORD = "Jite@12345"

VILLAGE = {
    1: "0113600723024/ आरसल पारसल/आरसल पारसल/116311",
    2: "0113600723024/ आरसल पारसल/नया गांव  नजीवावाद/116308",
    3: "0113600723008/ शिकारपुर/लौहर्रा इनायतगंज/116304",
    4: "0113600723008/ शिकारपुर/शिवनगर लौहारी/116305",
    5: "0113600723008/ शिकारपुर/लौहारी/116306",
    6: "0113600723008/ शिकारपुर/शिकारपुर/116307",
    7: "0113600723001/ पटटीकलां/पट्टी कला/116282"

}

FASAL = {"khareef": "link2",
         "rabi": "link3",
         "jayad": "link1"
         }

serv_obj = Service("chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
actions = ActionChains(driver)
mywait = WebDriverWait(driver, 10)

ttime = time.localtime()


def load_first_page():
    driver.get("http://164.100.59.148/")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"about_us\"]/div/div[2]/a").click()
    time.sleep(1)
    if ttime.tm_hour >= 9 and ttime.tm_hour <= 17:
        driver.find_element(By.XPATH,
                            "/html/body/center/main/div/div/ul/li[2]/a/div/div[1]").click()  # active before 4pm li[2]then li[4]
        time.sleep(1)
    else:
        driver.find_element(By.XPATH,
                            "/html/body/center/main/div/div/ul/li[4]/a/div/div[1]").click()  # active before 4pm li[2]then li[4]
        time.sleep(1)


def load_second_page():
    selectDistrict = Select(driver.find_element(By.ID, "up_district"))
    selectDistrict.select_by_visible_text("रामपुर")
    time.sleep(1)
    selectTehsil = Select(driver.find_element(By.ID, "up_tehsil"))
    selectTehsil.select_by_visible_text("स्वार")
    time.sleep(2)

    Select(driver.find_element(By.ID, "up_ri")).select_by_visible_text("0213600723001/ मसवासी")
    driver.find_element(By.ID, "password").send_keys(PASSWORD)

    time.sleep(12)
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[7]/button").click()
    time.sleep(2)


def load_third_page(vilage_name):
    print(vilage_name)
    # Select(driver.find_element(By.ID,"gram_name")).select_by_visible_text(VILLAGE[vilage_name]) #village name
    Select(driver.find_element(By.ID, "gram_name")).select_by_index(vilage_name)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"content1\"]/form/div[2]/button").click()


def load_fourth_page():
    driver.find_element(By.ID, FASAL["khareef"]).click()  # name of fasal to be locked
    time.sleep(5)
    try:
        while len(driver.find_elements(By.XPATH, "//input[@name=\"chk\"]")) != 0:
            check_box = driver.find_elements(By.XPATH, "//input[@name=\"chk\"]")
            print(len(check_box))
            for no in range(0,100):
                driver.execute_script("arguments[0].scrollIntoView();", check_box[no])
                
                if no < 15:
                    #time.sleep()
                    actions.move_to_element(check_box[no]).click().perform()
                    print("element clicked")
                else:
                    print("skipped")
            time.sleep(2)
            driver.find_element(By.XPATH, "//*[@id=\"printarea\"]/div[4]/form/button").click()
            time.sleep(5)

        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, "ri_remark"))
        driver.find_element(By.ID, "ri_remark").send_keys("approved")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/table/tbody/tr[2]/td/button").click()
        time.sleep(5)
    except:
        print("error")
        time.sleep(1)
        links = driver.find_elements(By.ID, "link3")
        links[1].click()
        time.sleep(2)


load_first_page()
load_second_page()

for i in range(19, 20):
    load_third_page(i)
    load_fourth_page()
