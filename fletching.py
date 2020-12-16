import time
import random
import pyautogui

logselection = input("What logs should we use? logs, oak, willow, maple \n")
randsleep = random.normalvariate(1, 0.4)
time.sleep(2)


def banking():
    print("Opening the bank...")
    chestdimensions = pyautogui.locateOnScreen('E:\\Desktop\\pycodes - kopie\\fletching\\bankchest.png', confidence=0.8)
    print(chestdimensions)
    chestX = random.uniform(chestdimensions[0]+(0.1*chestdimensions[2]), (chestdimensions[0]+(chestdimensions[2])*0.9))
    chestY = random.uniform(chestdimensions[1]+(0.1*chestdimensions[3]), (chestdimensions[1]+(chestdimensions[3])*0.9))
    dragdur = random.normalvariate(1, 0.2)
    pyautogui.moveTo(chestX, chestY, dragdur)
    pyautogui.click()
    time.sleep(randsleep)


def depositall():
    print("Depositing items...")
    depositdimensions = pyautogui.locateOnScreen(
        'E:\\Desktop\\pycodes - kopie\\fletching\\depositall.png', confidence=0.9)
    print(depositdimensions)
    depositx = random.uniform(depositdimensions[0]+(0.1*depositdimensions[2]), depositdimensions[0]+(depositdimensions[2])*0.9)
    deposity = random.uniform(depositdimensions[1]+(0.1*depositdimensions[3]), depositdimensions[1]+(depositdimensions[3])*0.9)
    dragdur = random.normalvariate(1, 0.2)
    pyautogui.moveTo(depositx, deposity, dragdur)
    pyautogui.click()
    time.sleep(randsleep)


def withdrawlogs():
    print("Withdrawing logs...")
    logdimensions = pyautogui.locateOnScreen(
        f'E:\\Desktop\\pycodes - kopie\\fletching\\{logselection}.png', confidence=0.9)
    logx = random.uniform(
        logdimensions[0]+(logdimensions[2]*0.1), logdimensions[0]+(logdimensions[2])*0.9)
    logy = random.uniform(
        logdimensions[1]+(logdimensions[3]*0.1), logdimensions[1]+(logdimensions[3])*0.9)
    dragdur = random.normalvariate(1, 0.2)
    pyautogui.moveTo(logx, logy, dragdur)
    pyautogui.click()
    time.sleep(randsleep)
    pyautogui.hotkey('esc')


def startfletch():
    # click on knife
    print('Clicking on the knife...')
    knifedimensions = pyautogui.locateOnScreen(
        'E:\\Desktop\\pycodes - kopie\\fletching\\invknife.png')
    knifex = random.uniform(
        knifedimensions[0]+(0.1*knifedimensions[2]), knifedimensions[0]+(knifedimensions[2])*0.9)
    knifey = random.uniform(
        knifedimensions[1]+(0.1*knifedimensions[3]), knifedimensions[1]+(knifedimensions[3])*0.9)
    dragdur = random.normalvariate(1, 0.2)
    pyautogui.moveTo(knifex, knifey, dragdur)
    pyautogui.click()
    time.sleep(randsleep)
    # click on log
    print('Clicking on the log...')
    logdimensions = pyautogui.locateOnScreen(
        f'E:\\Desktop\\pycodes - kopie\\fletching\\inv{logselection}.png', confidence=0.9)
    logx = random.uniform(
        logdimensions[0]+(logdimensions[2]*0.1), logdimensions[0]+(logdimensions[2])*0.9)
    logy = random.uniform(
        logdimensions[1]+(logdimensions[3]*0.1), logdimensions[1]+(logdimensions[3])*0.9)
    dragdur = random.normalvariate(1, 0.2)
    pyautogui.moveTo(logx, logy, dragdur)
    pyautogui.click()
    time.sleep(randsleep+0.5)

    #confirm last made object
    pyautogui.hotkey('space')
    #Waiting for inventory to complete
    print("Sleeping...")
    time.sleep(random.uniform(50, 54))

def startbot():
    try:
        banking()
        depositall()
        withdrawlogs()
        startfletch()
    except:
        pyautogui.hotkey('esc')
        return


while True:
    startbot()
