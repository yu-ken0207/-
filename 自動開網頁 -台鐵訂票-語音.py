from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()


chrome_options.add_argument("--start-maximized")     #最大化視窗
chrome_options.add_argument("--incognito")           #開啟無痕模式


driver = webdriver.Chrome()
driver.get("http://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query")



element = driver.find_element_by_name("pid");
element.send_keys("身分證號");#輸入內容




element = driver.find_element_by_name("startStation");
element.send_keys("地點");#輸入起點



element = driver.find_element_by_name("endStation");
element.send_keys("地點");#輸入終點



driver.find_element_by_id("rideDate1").clear();
element = driver.find_element_by_id("rideDate1");
element.send_keys("YYYMMDD");#輸入日期


element = driver.find_element_by_name("ticketOrderParamList[0].trainNoList[0]");
element.send_keys("###");#輸入車次

time.sleep(1)
click1=driver.find_element_by_id("switchToVoice")#切換換語音
click1.click()


click1=driver.find_element_by_id("playMusic")#播放語音
click1.click()










#click1=driver.find_element_by_id("recaptcha-audio-button")
#click1.click()

click1=driver.find_element_by_xpath(".//*[@dir='ltr']")
click1.click()

click1=driver.find_element_by_xpath(".//*[@value='訂票']")
click1.click()







#提交表單

#elem=driver.find_element_by_name("submit")
#elem.click()

#element.submit();
#driver.close()
