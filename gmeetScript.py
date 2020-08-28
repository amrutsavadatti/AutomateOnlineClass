from selenium import webdriver
from pynput.keyboard import Key ,Controller
import time,pytz
import datetime
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waitForElement(elem, selector_name):
    try:
        if selector_name == "id":
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, elem))
            )
        elif selector_name == "name":
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, elem))
            )
        elif selector_name == "xpath":
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, elem))
            )
        elif selector_name == "class name":
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, elem))
            )
    finally:
        pass

def newHandle():
    chromeDriver = os.path.join("chromedriver.exe")
    driver = webdriver.Chrome(chromeDriver)
    return driver


def openMeet(n):

    
    driver.get('https://meet.google.com/landing?authuser=1')

    waitForElement("identifier","name")#
    driver.find_element_by_name("identifier").send_keys(Email)#PUT EMAIL ID HERE

    waitForElement("//*[@id='identifierNext']/div/button/div[2]","xpath")#
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()

    #waitnig for a small time
    #driver.implicitly_wait(20)

    waitForElement("password","name")#
    driver.find_element_by_name("password").send_keys(Pass)#PUT YOUR PASSWORD HERE

    waitForElement("//*[@id='passwordNext']/div/button/div[2]","xpath")#
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()

    #driver.implicitly_wait(4)
    #clicking place to put classcode
    waitForElement("//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div","xpath")#
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div").click()


    #entering Meeting Code
    try:
        time.sleep(1)
        for char in classCodes[n]:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.12)
        waitForElement("//*[@id='yDmH0d']/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span/span","xpath")#
        driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span/span").click()
    except:
        print("error while entering meeting")
    try:
        #pressing Dismiss
        waitForElement("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div/span/span","xpath")#
        driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div/span/span").click()
        #pressing tab tab enter
        time.sleep(1)
        for i in range(2):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            time.sleep(0.12)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            time.sleep(0.12)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(1)
            
            
        time.sleep(1)
        driver.implicitly_wait(7)
        #Switching off Mic and Camera
        waitForElement("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div/span/span/div/div[1]","xpath")#
        driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div/span/span/div/div[1]").click()

        waitForElement("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div","xpath")#
        driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div").click()
        #entering the call
        
        waitForElement("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span","xpath")#
        driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()
            
    except:
        print("couldnt enter meeting or unable to control mic and camera")

def closeWindows():
    driver.quit()

def subtractTime(currTime,tt_Time):
    TT_time = datetime.datetime.combine(date, tt_Time)
    diff = (TT_time - current_timeDelta)
    return diff
def waitTillNext(nextLecture):
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).time()#Current Date
    current_timeDelta = datetime.datetime.combine(date,current_time)
    TT_time = datetime.datetime.combine(date, nextLecture)
    diff = (TT_time - current_timeDelta)
    print("waiting for {} minutes".format(diff.total_seconds()/60))
    time.sleep(diff.total_seconds()+15)

def waitForLect(lectTime):
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).time()#Current Date
    current_timeDelta = datetime.datetime.combine(date,current_time)
    TT_time = datetime.datetime.combine(date, lectTime)
    diff = (TT_time - current_timeDelta)
    print("lecture will be over in {} minutes ".format(diff.total_seconds()/60))
    time.sleep(diff.total_seconds()+180)

def isBetween(logInTime):

    if logInTime > datetime.time(12,00,00,000000) and logInTime < timeTable[2][0]:
        print("isBetween 12:00 and 12:10")
        waitTillNext(timeTable[2][0])
    elif logInTime > datetime.time(13,10,00,000000) and logInTime < timeTable[3][0]:
        print("isBetween 1:10 and 2:20")
        waitTillNext(timeTable[3][0])
    elif logInTime > datetime.time(15,20,00,000000) and logInTime < timeTable[4][0]:
        print("isBetween 3:20 and 3:30")
        waitTillNext(timeTable[4][0])

    

def callLecture():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).time()
    isBetween(current_time)
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).time()
    
    if current_time >= timeTable[1][0] and current_time < timeTable[2][0]:
        print("lecture 1")
        openMeet(timeTable[1][dow])
        waitForLect(datetime.time(12,00,00,000000))
        
        closeWindows()
        waitTillNext(timeTable[2][0])
        flag = 1
        return flag
    
    elif current_time >= timeTable[2][0] and current_time < datetime.time(13,10,00,000000):
        print("lecture 2")
        openMeet(timeTable[2][dow])
        waitForLect(datetime.time(13,10,00,000000))
        
        closeWindows()
        waitTillNext(timeTable[3][0])
        flag = 2
        return flag
        
    elif current_time >= timeTable[3][0] and current_time < datetime.time(15,30,00,000000):
        print("lecture 3")
        openMeet(timeTable[3][dow])
        waitForLect(datetime.time(15,20,00,000000))
        
        closeWindows()
        if dow == 5:
            flag = 4
            return flag
        waitTillNext(timeTable[4][0])
        flag = 3
        return flag
        
    elif current_time >= timeTable[4][0] and current_time < datetime.time(16,30,00,000000):
        print("lecture 4")
        openMeet(timeTable[4][dow])
        TT_time = datetime.datetime.combine(date, datetime.time(16,30,00,000000))
        diff = (TT_time - current_timeDelta)
        waitForLect(datetime.time(16,30,00,000000))
        closeWindows()
        flag = 4
    else:
        print("no match for time slot found")
        closeWindows()
        return 4

        
#****************************************************************************
#/////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
# Begins From Here

# put Your letures in this list if they are Different from this
classCodes = ["BECMPNA","BEMIS"]

timeTable = {1:[datetime.time(11,00,00,000000),0,1,0,1,0],2:[datetime.time(12,10,00,000000),0,0,0,0,0],3:[datetime.time(14,20,00,000000),0,0,0,0,0],4:[datetime.time(15,30,00,000000),0,0,1,0]}

#Put Your Accounts Email and Password Here

Email = "YOUR_EMAIL@student.sfit.ac.in"
Pass = "YOUR_PASSWORD"

#///////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#****************************************************************************
keyboard = Controller()
flag = 0
date = datetime.date(1,1,1)#Dummy Date
dow = datetime.datetime.today().weekday()#gives day of week in int
dow = dow + 1

print(dow)



if dow == 6 or dow == 7:
    print("Chill Maar, Weekend hai !!")
    exit(0)
    
#print(dow)

#Dictionary to store timetable timings and days of week
#{1:[time of lecture,mon,tue,wed,thur,fri]}


while (flag!= 4):
    driver = newHandle()
    
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).time()#Current Date
    current_timeDelta = datetime.datetime.combine(date,current_time)

    if current_time < timeTable[1][0]:
        print("invoked before time")
        print("waiting for the 11:00 am to begin lecture")
        waitTillNext(timeTable[1][0])
        continue
    #calling New Lectures
    flag = callLecture()

print("all executed correctly")
