from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException as SERE
import time
def scrollDown(count):
    for _ in range(count+2):
        driver.find_element_by_xpath("//body").send_keys(Keys.ARROW_DOWN)

driver = webdriver.Chrome(executable_path="D:\\Study\\Automation\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.amazon.jobs/en/")
driver.maximize_window()
driver.find_element_by_xpath("(//a[text()='Your job application'])[2]").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@name='email']").send_keys("shubhamawasthi06@gmail.com")
driver.find_element_by_xpath("//button[text()='Continue']").click()
driver.implicitly_wait(120)
driver.find_element_by_xpath("//input[@name='password']").send_keys("Amsterdam100%") 
driver.find_element_by_xpath("//button[text()='Sign In']").click()
driver.implicitly_wait(120)
driver.find_element_by_xpath("//a[@aria-label='menu']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//a[text()='Job categories']").click()
driver.implicitly_wait(120)
driver.find_element_by_xpath("//input[@name='base_query']").send_keys("Software Development Engineer in Test") 
driver.find_element_by_xpath("//input[@name='loc_query']").send_keys("India") 
driver.find_element_by_xpath("//button[@aria-label='Search jobs']").click()
driver.implicitly_wait(120)
driver.find_element_by_xpath("//button[@data-toggle='dropdown']").click()
driver.find_element_by_xpath("//a[@id='recent']").click()
driver.implicitly_wait(120)
count_of_jobs = driver.find_element_by_xpath("//div[@class='col-sm-6 job-count-info']").text
print("Total jobs found: ",count_of_jobs)
time.sleep(10)
for i in range(1,10):
    scrollDown(i)
    driver.find_element_by_xpath("(//div[@class='job-tile'])"+"["+str(i)+"]").click()
    content = driver.find_element_by_xpath("//div[@class='section']/p").text
    if 'years' or 'year' in content:
        pos = content.index('years')
        print(content[pos-3:pos+5])
    else:
        continue
    driver.back()
    time.sleep(10)

