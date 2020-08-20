from selenium import webdriver
from pynput.keyboard import Key ,Controller
import time,pytz
import datetime
import os

def newHandle():
    chromeDriver = os.path.join("chromedriver.exe")
    driver = webdriver.Chrome(chromeDriver)
    return driver


def openMeet(n):

    
    driver.get('https://meet.google.com/landing?authuser=1')

    driver.find_element_by_name("identifier").send_keys(Email)#PUT EMAIL ID HERE
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()

    #waitnig for a small time
    driver.implicitly_wait(10)

    driver.find_element_by_name("password").send_keys(Pass)#PUT YOUR PASSWORD HERE

    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()

    driver.implicitly_wait(4)
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div").click()


    #entering Meeting Code
    try:
        driver.implicitly_wait(4)
        time.sleep(1)
        for char in classCodes[n]:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.12)
        driver.implicitly_wait(7)
        driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span/span").click()
    except:
        print("error while entering meeting")
    try:
        #pressing Dismiss
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
        driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div/span/span/div/div[1]").click()
        driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div").click()
        #entering the call
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
    time.sleep(diff.total_seconds())

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
    isBetween(current_time)
    
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
        
    elif current_time >= timeTable[3][0] and current_time < timeTable[4][0]:
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

Email = "amrutsavadatti@student.sfit.ac.in"
Pass = "Amrutsavadatti16"

#///////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#****************************************************************************
keyboard = Controller()
flag = 0
date = datetime.date(1,1,1)#Dummy Date
dow = datetime.datetime.today().weekday()#gives day of week in int
dow = dow + 1# only for my pc else +1 for other pcs
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
    











'''    
#print(dow)
openMeet(timeTable[4][dow])
time.sleep(120)
'''



