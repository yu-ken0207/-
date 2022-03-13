from selenium import webdriver
import time
import pyautogui

chrome_options = webdriver.ChromeOptions()


#chrome_options.add_argument("--start-maximized")     #最大化視窗
chrome_options.add_argument("--incognito")           #開啟無痕模式


driver = webdriver.Chrome()
driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query")

#driver.maximize_window()    #最大化視窗

element = driver.find_element_by_name("pid");
element.send_keys("u122093329");#輸入內容




element = driver.find_element_by_name("startStation");
element.send_keys("7000-花蓮");#輸入起點



element = driver.find_element_by_name("endStation");
element.send_keys("3300-臺中");#輸入終點



driver.find_element_by_id("rideDate1").clear();
element = driver.find_element_by_id("rideDate1");
element.send_keys("20200628");#輸入日期


element = driver.find_element_by_name("ticketOrderParamList[0].trainNoList[0]");
element.send_keys("283");#輸入車次

time.sleep(1)

pyautogui.moveTo(927, 775,1) #移動

pyautogui.click()   #點擊

#click1=driver.find_element_by_id("switchToVoice")#切換換語音
#click1.click()


#click1=driver.find_element_by_id("playMusic")#播放語音
#click1.click()










#click1=driver.find_element_by_id("recaptcha-audio-button")
#click1.click()

#click1=driver.find_element_by_xpath(".//*[@dir='ltr']")
#click1.click()

#click1=driver.find_element_by_xpath(".//*[@value='訂票']")
#click1.click()







#提交表單

#elem=driver.find_element_by_name("submit")
#elem.click()

#element.submit();
#driver.close()
