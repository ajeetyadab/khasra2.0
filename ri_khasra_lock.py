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


PASSWORD = "Anoop@123"

VILLAGE = ["0113600723036/ हरदासपुर कोठरा/पैगम्वर पुर/116370",
		   "0113600723036/ हरदासपुर कोठरा/हरदासपुर कौठरा/116377",
		   "0113600723036/ हरदासपुर कोठरा/मडैयान भज्जन/116368",
		   "0113600723036/ हरदासपुर कोठरा/हरनगला/116374",
		   "0113600723036/ हरदासपुर कोठरा/पृथीनगर/116373",
		   "0113600723019/ खेमपुर/रसूलपुर फरीदपुर/116364"
		   ]

FASAL = {"khareef":"link2",
         "rabi": "link3",
         "jayad": "link1"
        }


serv_obj=Service("chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
actions=ActionChains(driver)
mywait=WebDriverWait(driver,10)

ttime = time.localtime()

def load_first_page():
    driver.get("http://164.100.59.148/")
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id=\"about_us\"]/div/div[2]/a").click()
    time.sleep(1)
    if ttime.tm_hour >= 9 and ttime.tm_hour <=17:
        driver.find_element(By.XPATH, "/html/body/center/main/div/div/ul/li[2]/a/div/div[1]").click() # active before 4pm li[2]then li[4]
        time.sleep(1)
    else:   
        driver.find_element(By.XPATH, "/html/body/center/main/div/div/ul/li[4]/a/div/div[1]").click() # active before 4pm li[2]then li[4]
        time.sleep(1)

def load_second_page():
	selectDistrict = Select(driver.find_element(By.ID, "up_district"))
	selectDistrict.select_by_visible_text("रामपुर")
	time.sleep(1)
	selectTehsil = Select(driver.find_element(By.ID, "up_tehsil"))
	selectTehsil.select_by_visible_text("स्वार")
	time.sleep(3)
    
	Select(driver.find_element(By.ID, "up_ri")).select_by_visible_text("0213600723003/ समोदिया")
	driver.find_element(By.ID, "password").send_keys(PASSWORD)
    
	time.sleep(15)
	driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[7]/button").click()
	
def load_third_page():
	Select(driver.find_element(By.ID,"gram_name")).select_by_visible_text(VILLAGE[1]) #village name

	time.sleep(1)
	driver.find_element(By.XPATH, "//*[@id=\"content1\"]/form/div[2]/button").click()
	
def load_fourth_page():
	driver.find_element(By.ID, FASAL["rabi"]).click() # name of fasal to be locked
	time.sleep(20)
		
	while len(driver.find_elements(By.XPATH,"//input[@name=\"chk\"]")) !=0:
		check_box = driver.find_elements(By.XPATH,"//input[@name=\"chk\"]")
		print(len(check_box))
		for boxes in check_box:
			driver.execute_script("arguments[0].scrollIntoView();", boxes)
			time.sleep(.5)
			actions.move_to_element(boxes).click().perform()
			print("element clicked")
	
		driver.find_element(By.XPATH, "//*[@id=\"printarea\"]/div[4]/form/button").click()
		time.sleep(20)
	


	

	
load_first_page()
load_second_page()
load_third_page()
load_fourth_page()


