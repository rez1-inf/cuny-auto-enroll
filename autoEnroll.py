from platform import release
from datetime import datetime
import platform
import pyautogui
import time
import sys
import os.path
from os import listdir
import os

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

count = 0
sleepTime = 300
enrolled = False
loggedIn = False
samplesDir = 'Samples/'
samples = None
termSet = False
term = None
OS_Info = platform.system()
pixelRatio = pyautogui.screenshot().size[0]/pyautogui.size().width

# check screen resolution and set sample directory
x, y = pyautogui.size()
samplesDir += str(x) +"x"+ str(y) +"/"

# Create samples directory for current screen resolution if it doesn't exist
if os.path.exists(samplesDir) is False:
    os.mkdir(samplesDir)
    print("Please put the samples in " + samplesDir + " directory and then re-run this script")
    sys.exit(0)

# check if all the files exist in the Samples directory
while True:
    tryAgain = False
    if len(listdir(samplesDir)) != 11:
        if platform.system() == 'Darwin':
            if os.path.exists(samplesDir + ".DS_Store"):
                os.remove(samplesDir + ".DS_Store")
                tryAgain = True
        if not tryAgain:
            print("There needs to be EXACTLY 11 sample screenshots inside the " + samplesDir +" directory.")
            print("Please make sure there are no hidden and/or unusable files in that directory. Quitting")
            sys.exit(1)
    else:
        samples = listdir(samplesDir)
        samples.sort()
        for i in range(0, 9):
            if samples[i][0] != "0":
                print("First 9 files need to start with \"0\"")
                print("eg: 05.png... Please rename.. Quitting")
                sys.exit(2)
        break

# get a sample file location
def getSample(sampleNum):
    return (samplesDir + samples[sampleNum-1])

# click based on OS (MacOS needs correction in coordinates)
def click(sampleNum):
    coordinates = pyautogui.locateCenterOnScreen(getSample(sampleNum))
    if coordinates is not None:
        x = coordinates[0]/pixelRatio
        y = coordinates[1]/pixelRatio
        if OS_Info == "Darwin": # if macOS
            coordinates = pyautogui.locateCenterOnScreen(getSample(2)) # click on browser berfore clicking target (macOS issue)
            pyautogui.click(coordinates[0]/pixelRatio, coordinates[1]/pixelRatio)   #click cunyFirst logo first
            pyautogui.click(x, y)   # main target to click
        else:
            pyautogui.click(x, y)
        return True
    else:
        return False

# move mouse to
def moveTo(sampleNum):
    coordinates = pyautogui.locateCenterOnScreen(getSample(sampleNum))
    if coordinates is not None:
        x = coordinates[0]/pixelRatio
        y = coordinates[1]/pixelRatio
        pyautogui.moveTo(x, y)
        return True
    else:
        return False


# click based on x, y coordinates
def clickCoord(coordinates):
    if OS_Info == "Darwin":
        x = coordinates[0]/pixelRatio
        y = coordinates[1]/pixelRatio
        click(2)
        pyautogui.click(x+5, y+5)   # offset by 5 pixel in macOS
    else:
        pyautogui.click(coordinates)

# choose a term
def takeTermInput(coordinates):
    num = input("Enter a number from 1 - "+str(len(coordinates))+": ")
    num = int(num)
    if num > 0 and num <= len(coordinates):
        return (num -1)
    else:
        takeTermInput()

# relogin if something goes wrong and try again
def re_login():
    ret = click(2)
    if ret is False:
        print("Can't locate browser for CUNY. Quitting")
        print("Please replace sample for: " + getSample(2) +"\n")
        sys.exit(3)
    if OS_Info == "Darwin":
        pyautogui.hotkey('command', 'l')
    else:
        pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)
    pyautogui.typewrite("home.cunyfirst.cuny.edu")
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(5)

# logs in to CUNYFirst from start page
def initialLogin():
    ret = click(1)
    if ret is True:
        time.sleep(5)
        return True
    else:
        print("Can't find initial login button")
        print("If it keeps happening, please replace sample for: " + getSample(1) +"\n")
        return False

# goto student center 
def gotoStudentCenter():
    ret = click(3)
    if ret is True:
        time.sleep(5)
        return True
    else:
        print("Can't find Student Center")
        print("If it keeps happening, please replace sample for: " + getSample(3) +"\n")
        return False

# goto plan in student center
def gotoPlan():
    ret = click(4)
    if ret is True:
        time.sleep(5)
        return True
    else:
        print("Can't find 'plan' in student center")
        print("If it keeps happening, please replace sample for: " + getSample(4) +"\n")
        return False

# clicks the shopping cart
def clickCart():
    ret = click(5)
    if ret is True:
        time.sleep(5)
        return True
    else:
        print("Can't find Shopping Cart")
        print("If it keeps happening, please replace sample for: " + getSample(5) +"\n")
        return False

# click a term
def clickTerm():
    global term
    global termSet
    isVisible(7)    # make sure continue button is visible (hence all terms as well)
    if termSet:
        coordinates = list(pyautogui.locateAllOnScreen(getSample(6)))
        if coordinates is not None and len(coordinates) >= 1:
            clickCoord(coordinates[term])
            time.sleep(1)
            return True
        else:
            print("Expected term selection page but can't find. Trying to re-login (reset)")
            return False
    else:
        coordinates = list(pyautogui.locateAllOnScreen(getSample(6)))
        if coordinates is not None and len(coordinates) >= 1:
            if OS_Info == "Darwin":
                pyautogui.hotkey('command', 'tab')
            else:
                pyautogui.hotkey('alt', 'tab')
            time.sleep(1)
            print("There are " + str(len(coordinates)) +" terms on the screen")
            print("Please select one")
            term = takeTermInput(coordinates)
            time.sleep(1)
            clickCoord(coordinates[term])
            termSet = True
            time.sleep(1)
            return True
        else:
            print("Expected term selection page but can't find. Trying to re-login (reset)")
            print("If it keeps happening, please replace sample for: " + getSample(6) +"\n")
            return False

# clicks continue after selecting a term
def clickContinue():
    ret = click(7)
    if ret is True:
        time.sleep(5)
        return True
    else:
        print("Can't find continue button")
        print("If it keeps happening, please replace sample for: " + getSample(7) +"\n")
        return False

# click a single check box for 1 open class (this is used in a loop from caller)
def clickCheckBox(checkBoxes, openClass):
    minDiff = 999999999
    index = -1
    count = 0
    y2 = openClass[1]
    for box in checkBoxes:
        y1 = box[1]
        diff = abs(y2 - y1)
        if minDiff > diff:
            minDiff = diff
            index = count
        count += 1
    clickCoord(checkBoxes[index])

# scroll to make sure something (a button for example) is visible
def isVisible(sampleNum):
    tryCount = 0
    while True:
        if pyautogui.locateCenterOnScreen(getSample(sampleNum)) is None:
            pyautogui.scroll(-2)
            tryCount += 1
            if tryCount == 5:
                print("Cant find "+ getSample(sampleNum) +"\nPlease get new screenshot for that sample")
                sys.exit(4)
        else:
            break


while enrolled == False:
    one = initialLogin()
    two = gotoStudentCenter()
    three = gotoPlan()
    if one == False and two == False and three == False:
        re_login()
    else:
        loggedIn = True

    while loggedIn == True and enrolled == False:
        if clickTerm() == False:
            loggedIn = False
            break
        if clickContinue() == False:
            loggedIn = False
            break

        isVisible(9)    # make sure (enroll button is visible) hence all classes are visible
        moveTo(9)   # to avoid blocking green status buttons on screen by the mouse

        gLight = list(pyautogui.locateAllOnScreen(getSample(11)))
        if len(gLight) == 0:    # if no class is open
            count = count + 1
            pyautogui.scroll(50)
            print("Try Count: " + str(count) + " (wait " + str(sleepTime/60) +" min) [" + datetime.now().strftime("%h %d - %I:%M %p") + "]")
            if count % 10 == 0:
                print("Note: if you can observe an open class and this script is not noticing it,\nthen please replace sample for: " + getSample(11) +"\n")
            time.sleep(sleepTime)
        else:
            checkBoxes = list(pyautogui.locateAllOnScreen(getSample(8)))
            if len(checkBoxes) < len(gLight):
                print("# of check boxes are less than open classes. Re-Trying")
                print("If it keeps happening, please replace sample for: " + getSample(8) +"\n")
                loggedIn = False
                break

            print("Found: " + str(len(gLight)) +" classes open")

            # select all available classes
            for openClass in gLight:
                clickCheckBox(checkBoxes, openClass)
            
            time.sleep(1)

            # finish enrolling in open classes
            enroll = click(9)
            if enroll is False:
                print("Can't find enroll button")
                print("If it keeps happening, please replace sample for: " + getSample(9) +"\n")
                loggedIn = False
                break
            time.sleep(5)

            isVisible(10)   # make sure finish enroll button is visible
            fEnroll = click(10)
            if fEnroll is False:
                print("Can't find Finish Enroll button")
                print("If it keeps happening, please replace sample for: " + getSample(10) +"\n")
                loggedIn = False
                break
            print("Enrolled [" + datetime.now().strftime("%h %d - %I:%M %p") + "]")
            enrolled = True
            break

        if clickCart() == False:
            loggedIn = False
            break;
