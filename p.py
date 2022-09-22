from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class orangeHRM_page():

    url = "https://opensource-demo.orangehrmlive.com"
    driver = webdriver.Firefox()


    def Login_page(self):

        username = "Admin" 
        password = "admin123"
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(5)
        
        username_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        password_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        login_button_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

        username1 = self.driver.find_element(by=By.XPATH, value=username_xpath)
        password1 = self.driver.find_element(by=By.XPATH, value=password_xpath)
        login_button = self.driver.find_element(by=By.XPATH, value=login_button_xpath)

        username1.send_keys(username)
        time.sleep(5)
        password1.send_keys(password)
        time.sleep(5)
        login_button.click()
        time.sleep(5)

        Add_Employee = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a')
        time.sleep(5)
        Add_Employee.click()
        time.sleep(5)
        
        Employeenamef = "Yash"
        Employeenamem = "raj"
        Employeenamel = "E"
        time.sleep(5)
        
        Employeename1_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
        Employeename2_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
        Employeename3_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
        
        Employeename1 = self.driver.find_element(by=By.XPATH, value=Employeename1_xpath)
        Employeename2 = self.driver.find_element(by=By.XPATH, value=Employeename2_xpath)
        Employeename3 = self.driver.find_element(by=By.XPATH, value=Employeename3_xpath)
        
        Employeename1.send_keys(Employeenamef)
        time.sleep(5)
        Employeename2.send_keys(Employeenamem)
        time.sleep(5)
        Employeename3.send_keys(Employeenamel)
        time.sleep(5)
       
        Create_detail = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span')
        time.sleep(5)
        Create_detail.click()
        time.sleep(5)

        username = "Gokul"
        Password = "Gokul@2022"
        Confirm_Password = "Gokul@2022"
        time.sleep(5)

        Username_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
        Password_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
        Confirm_Password_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'

        Username1 = self.driver.find_element(by=By.XPATH, value=Username_xpath)
        Password1 = self.driver.find_element(by=By.XPATH, value=Password_xpath)
        Confirm_Password1 = self.driver.find_element(by=By.XPATH, value=Confirm_Password_xpath)

        Username1.send_keys(username)
        time.sleep(5)
        Password1.send_keys(Password)
        time.sleep(5)
        Confirm_Password1.send_keys(Confirm_Password)
        time.sleep(5)

        Save_button = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        time.sleep(5)
        Save_button.click()
        time.sleep(5)

        Admin_section = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
        time.sleep(5)
        Admin_section.click()
        time.sleep(5)


        username = "Gokul"
        Employeename = "Yash" 
        time.sleep(5)

        username_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
        Employeename_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input'
        search_button_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'

        username1 = self.driver.find_element(by=By.XPATH, value=username_xpath)
        Employeename1 = self.driver.find_element(by=By.XPATH, value=Employeename_xpath)
        search_button = self.driver.find_element(by=By.XPATH, value=search_button_xpath)

        username1.send_keys(username)
        time.sleep(5)
        Employeename1.send_keys(Employeename)
        time.sleep(5)
        search_button.click()
        time.sleep(5)

        logout1 = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p')
        time.sleep(5)
        logout1.click()
        time.sleep(5)

        logout = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a')
        time.sleep(5)
        logout.click()
        time.sleep(5)

    def login(self):

        username = "Gokul" 
        password = "Gokul@2022"
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(5)
        
        username_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        password_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        login_button_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

        username1 = self.driver.find_element(by=By.XPATH, value=username_xpath)
        password1 = self.driver.find_element(by=By.XPATH, value=password_xpath)
        login_button = self.driver.find_element(by=By.XPATH, value=login_button_xpath)

        username1.send_keys(username)
        time.sleep(5)
        password1.send_keys(password)
        time.sleep(5)
        login_button.click()
        time.sleep(5)
    

    def close(self):
        self.driver.close()
        time.sleep(5)



o = orangeHRM_page()

o.Login_page()

o.login()

o.close()
