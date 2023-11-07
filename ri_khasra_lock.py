from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support import expected_conditions
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

VILLAGE = {
    
           1:'0113600723036/ हरदासपुर कोठरा/पैगम्वर पुर/116370',
		   2:'0113600723036/ हरदासपुर कोठरा/हरदासपुर कौठरा/116377',
		   3:'0113600723036/ हरदासपुर कोठरा/मडैयान भज्जन/116368',
		   4:'0113600723036/ हरदासपुर कोठरा/हरनगला/116374',
		   5:'0113600723036/ हरदासपुर कोठरा/पृथीनगर/116373',
		   6:'0113600723019/ खेमपुर/रसूलपुर फरीदपुर/116364',
           7:'0113600723019/ खेमपुर/खेमपुर/116367',
           8:'0113600723019/ खेमपुर/चाँदपुर/116366',
           9:'0113600723019/ खेमपुर/पसियापुरा/116365',
           10:'0113600723019/ खेमपुर/रसूलपुर फरीदपुर/116364',
           11:'0113600723038/ ढाैकपुरी टाण्‍डा/खेड़ा टांडा/116381',
           12:'0113600723038/ ढाैकपुरी टाण्‍डा/ढोकपुरी टांडा/116382',
           13:'0113600723038/ ढाैकपुरी टाण्‍डा/मुस्तफावाद ढोकपुरी/116383',
           14:'0113600723038/ ढाैकपुरी टाण्‍डा/साल्वे नगर/116385',
           15:'0113600723035/ भोट वक्‍काल/इमरती/116379',
           16:'0113600723035/ भोट वक्‍काल/भोट वक्काल/116380',
           17:'0113600723035/ भोट वक्‍काल/शादीनगर नि.हरदासपुर/116378',
           18:'0113600723035/ भोट वक्‍काल/शाहदरा भोट/116376',
           19:'0113600723017/ मधुपुरा/छपर्रा/116343',
           20:'0113600723017/ मधुपुरा/मधुपुरा/116341',
           21:'0113600723017/ मधुपुरा/रुस्तमनगर निकट छपर्रा/116342',
           22:'0113600723016/ लखीमपुर/असालतपुर/116350',
           23:'0113600723016/ लखीमपुर/धनौरा/116344',
           24:'0113600723016/ लखीमपुर/मुकरमपुर/116347',
           25:'0113600723016/ लखीमपुर/लखीमपुर/116348',
           26:'0113600723016/ लखीमपुर/लाड़पुर नि.वथुआखेड़ा/116349',
           27:'0113600723016/ लखीमपुर/शिवनगर नि.असालतपुर/116351',
           28:'0113600723016/ लखीमपुर/सैदनगर नि.असालतपुर/116346',
           29:'0113600723033/ विझडा/कुंवरपुर नानकार/116401',
           30:'0113600723033/ विझडा/नवी गंज नि.वथुआखेड़ा/116399',
           31:'0113600723033/ विझडा/महुआ खेड़ा स्वार/116352',
           32:'0113600723033/ विझडा/विझडा/116400',
           33:'0113600723037/ शिवपुरी/गम्मनपुरा/116372',
           34:'0113600723037/ शिवपुरी/छत्तरपुर/116384',
           35:'0113600723037/ शिवपुरी/मल्हपुरा/116375',
           36:'0113600723037/ शिवपुरी/रजपुरा स्वार/116371',
           37:'0113600723037/ शिवपुरी/शिवपुरी/116369',
           38:'0113600723037/ शिवपुरी/सईदनगर उर्फ मडै0पूसे/116420',
           39:'0113600723020/ समोदिया/इमरतपुर/116360',
           40:'0113600723020/ समोदिया/खरदिया/116361',
           41:'0113600723020/ समोदिया/मिलक असद खाँ/116357',
           42:'0113600723020/ समोदिया/मिलक काजी/116355',
           43:'0113600723020/ समोदिया/मिलक गुलाम खाँ/116358',
           44:'0113600723020/ समोदिया/वथुआ खेड़ा/116359',
           45:'0113600723020/ समोदिया/शाहदरा नि.धनपुर/116354',
           46:'0113600723020/ समोदिया/समोदिया/116356',
           47:'0113600723018/ सोनकपुर/अजीमनगर/116362',
           48:'0113600723018/ सोनकपुर/धनपुर नि.शाहदरा/116353',
           49:'0113600723018/ सोनकपुर/सोनकपुर/116363',
}


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
	time.sleep(2)
	
def load_third_page(vilage_name):
	Select(driver.find_element(By.ID,"gram_name")).select_by_visible_text(VILLAGE[vilage_name]) #village name

	time.sleep(1)
	driver.find_element(By.XPATH, "//*[@id=\"content1\"]/form/div[2]/button").click()
	
def load_fourth_page(village_name):
    driver.find_element(By.ID, FASAL["khareef"]).click() # name of fasal to be locked
    time.sleep(12)
    try:
         driver.find_elements(By.XPATH,"//input[@name=\"chk\"]")
         while len(driver.find_elements(By.XPATH,"//input[@name=\"chk\"]")) !=0:
            check_box = driver.find_elements(By.XPATH,"//input[@name=\"chk\"]")
            print(len(check_box))
            for boxes in check_box:
                driver.execute_script("arguments[0].scrollIntoView();", boxes)
                time.sleep(.5)
                actions.move_to_element(boxes).click().perform()
                print("element clicked")
        
            driver.find_element(By.XPATH, "//*[@id=\"printarea\"]/div[4]/form/button").click()
            time.sleep(12)
         driver.find_element(By.ID,"ri_remark").send_keys("approved")
         time.sleep(10)
    except NoSuchElementException:
        pass
    load_third_page(village_name)
    load_fourth_page()
	


	

for i in range(11,50):
    load_first_page()
    load_second_page()
    load_third_page(i)
    load_fourth_page(i)


