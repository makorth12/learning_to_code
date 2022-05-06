import queue
import cv2 as cv
import numpy as np
import os
import pyautogui as py
import glob
import time
import shutil
import pygetwindow
import queue
import threading
import time
from threading import Thread
from windowcapture import WindowCapture
from keypoint_vision import Keypoint_Vision
from matchTemplate_vision import MatchTemplate_Vision
from pynput.keyboard import Controller
from os import path
from PIL import ImageGrab


keyboard = Controller()

# Change the working directory to the folder this script is in.
os.chdir(r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual')

avoid = glob.glob(r"C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\defeat\test\*.png")

victory_directory = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\victory'
defeat_directory = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\defeat'
timeout_directory = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\timeout'

victory_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\victory.png'
defeat_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\defeat.png'
timeout_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\timeout.png'
escape_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\escape.png'

ammo = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\ammo\ammo.png'
level = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\levelup\arrow.png'
refit = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\refit\shipReadyToRefitIcon.png'
pvp = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\pvp\pvp.png'
attack_img = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\attack\attack.png'

items = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\items.png'
item_repair = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\item_repair.png'

galaxy = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\galaxy.png'
health = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\health.png'
shipDamaged = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\shipDamaged.png'

league_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\league_image.png'
profile_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\profile_image.png'
fleet_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\fleet_image.png'
ladder_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\ladder__image.png'
bank_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\bank_image.png'
captain_cleared_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\captaincleared_image.png'
shop_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\shop_image.png'
another_user_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\another_user_image.png'

reload = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\reload.png'
reconnect = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\reconnect.png'
connectionError = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\connectionError.png'


gas = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\rss\gas.png'
minerals = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\rss\mins.png'

currency_gas_location = 422, 545
currency_min_location = 412, 481

# initialize the WindowCapture class
# left blank to capture the whole screen
app_window = WindowCapture()

level_icon = MatchTemplate_Vision(level)
level_x_0, level_x_1 = 560, 860
level_y_0, level_y_1 = 750, 870
level_x_adjustment = 0
level_y_adjustment = 0

yes = 1091, 606

def pvp_check():
    while True:
        foundPVP = py.locateCenterOnScreen(pvp, region=(540, 874, 1381-540, 1033-874), confidence=0.94, grayscale=True) 
        if foundPVP != None:
            time.sleep(1)
            print('Clicking PvP...')
            time.sleep(1)
            py.click(foundPVP)
            print('Clicked PvP!')
            time.sleep(1)
            ShipDamage()
            time.sleep(1)

def refit_check():
    while True:
        foundRefit = py.locateCenterOnScreen(refit, region=(10, 130, 150-10, 220-130), confidence=0.94, grayscale=True)
        if foundRefit != None:
            return True

def ammo_reload():
    foundAmmo = py.locateCenterOnScreen(ammo, region=(1800, 750, 1890-1800, 800-750), confidence=0.94, grayscale=True)
    if foundAmmo != None:
        x = foundAmmo[0]
        y = foundAmmo[1]
        print("Reloading ship...")
        py.click(foundAmmo)
        time.sleep(1)
        py.click(x+-1120,y+-95)
        print("Ship reload complete!")
                     
def repair(yes):
  
    bux_repair_pixel_x = 535
    bux_repair_pixel_y = 68
    item_repair_pixel_x = 443
    item_repair_pixel_y = 68
  
    for z in range (0, 10):
        galaxy_button = py.locateOnScreen(galaxy, region=(1771,918,1904,1029), confidence=0.92)
        health_bar = py.locateOnScreen(health, region=(427,55,561,80), confidence=0.92)
        items_menu = py.locateCenterOnScreen(items, region=(194, 978, 265, 1029), confidence=0.92)        
    
        if galaxy_button and health_bar != None:
            r,g,b = py.pixel(item_repair_pixel_x, item_repair_pixel_y)
            if g == 49 and items_menu != None:
                print("Reparing ship with an item...")
                py.click(items_menu)
                time.sleep(1)
                repair_item = py.locateCenterOnScreen(item_repair, region=(16, 938, 93, 1023), confidence=0.92)
                py.click(repair_item)
                time.sleep(1)
                py.click(825, 664)
                time.sleep(1)
                py.click(yes)
                time.sleep(1)
                click_ok()
                time.sleep(1)
                print("Ship repaired with an item!")
                time.sleep(3)

            if galaxy_button and health_bar != None:
                r,g,b = py.pixel(bux_repair_pixel_x, bux_repair_pixel_y)
                if g == 49:
                    print("Reparing ship with bux...")
                    py.click(bux_repair_pixel_x, bux_repair_pixel_y)
                    time.sleep(1)
                    py.click(yes)
                    print("Ship repaired with bux!")
                    time.sleep(3)
        
def levelup(object, y_0, y_1, x_0, x_1, x_adjustment, y_adjustment):
    for z in range (0, 10):
        haystack = app_window.get_haystack()
        location = haystack[y_0:y_1, x_0:x_1]
        img = object.find(location, 0.92, 'points1','levelup')
       
        if img:
            x_coord = img[0][0] + x_0
            y_coord = img[0][1] + y_0
            print("Levelling up...")
            py.click(x_coord+15,y_coord+30)
            time.sleep(1)
            py.click(x_coord+120,y_coord+110)
            time.sleep(1)
            py.click(x_coord-100,y_coord-100)
            time.sleep(1)
            print("Levelled up!")

def loadImages(directory):
	# Intialise empty array
	image_list = []
	# Add images to array
	for i in directory:
		img = cv.imread(i, cv.IMREAD_UNCHANGED)
		image_list.append((img, i))
	return image_list

def videoLoop():
    # Grab PSS Window and find size 
    window = pygetwindow.getWindowsWithTitle('Pixel Starships')[0]
    x1 = window.left
    y1 = window.top
    height = window.height
    width = window.width
    x2 = x1 + width
    y2 = y1 + height
    # Actual Video Loop, cropped down to the specific window,
    # resized to 1/2 size, and converted to BGR for OpenCV
    haystack_img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    crop = haystack_img.crop((750,30,1150,78))
    haystack_img_np = np.array(crop)
    haystack = cv.cvtColor(haystack_img_np, cv.COLOR_BGR2GRAY)
    
    cv.imshow("Ship Detection", haystack)
    cv.moveWindow("Ship Detection",1,-400)
    cv.waitKey(1)       
    return haystack

def shipDetection(image_list):
    # Object Detection
    counter = 0
    # start timer

    t0 = time.time()
    nbLoop = len(image_list)

    for i, img in enumerate(image_list):

        counter += 1       
        needle_img = img[0]
        needle_name = img[1]
        sliced_name = needle_name.split("\\")[-1]
        
        # load image to find
        objectToFind = Keypoint_Vision(needle_img)
        # get an updated image of the screen
        keypoint_haystack = app_window.get_haystack()
        # crop the image
        x, w, y, h = [700,500,30,85]
        keypoint_haystack = keypoint_haystack[y:y+h, x:x+w]

        kp1, kp2, matches, match_points, log = objectToFind.match_keypoints(keypoint_haystack, sliced_name, counter, min_match_count=60)
        match_image = cv.drawMatches(objectToFind.needle_img, kp1, keypoint_haystack, kp2, matches, None)

        # display the processed image
        cv.imshow('Keypoint Search', match_image)
        cv.moveWindow("Keypoint Search",1,-200)
        cv.waitKey(1)       

        if match_points:
            # find the center point of all the matched features
            center_point = objectToFind.centeroid(match_points)
            # account for the width of the needle image that appears on the left
            center_point[0] += objectToFind.needle_w
            # drawn the found center point on the output image
            match_image = objectToFind.draw_crosshairs(match_image, [center_point])
       
            # display the processed image
            cv.imshow('Keypoint Search', match_image)
            cv.moveWindow("Keypoint Search",1,-200)
            cv.waitKey(1)       

            keep_looking(log)
            time.sleep(1)

            ts = time.time() - t0
            tdp = "{:.2f}".format(ts)
            print('Loop Time:',tdp)

            return True  

        
    ts = time.time() - t0
    tdp = "{:.2f}".format(ts)
    print('Loop Time:',tdp)

    return False



def prepare_objectDetection():
    print("Preparing Object Detection...")
    py.moveTo(921, 415)
    time.sleep(1)
    py.dragTo(921, 815, 1, button='left')
    print("Finished preparing Object Detection!")

def attack():
    py.moveTo(1415,1000,0.1)
    time.sleep(0.01)
    attackLog()
    py.click()
    time.sleep(3)

def click_random():
    while True:
        foundCaptainCleared = py.locateCenterOnScreen(captain_cleared_image, region=(661, 483, 1040-661, 591-483), confidence=0.94, grayscale=True)
        foundAnotherUser = py.locateCenterOnScreen(another_user_image, region=(678, 444, 1221-678, 606-444), confidence=0.94, grayscale=True)
        foundReload = py.locateCenterOnScreen(reload, region=(830, 630, 1080-830, 720-630), confidence=0.94, grayscale=True)
        foundReconnect = py.locateCenterOnScreen(reconnect, region=(678, 444, 1221-678, 606-444), confidence=0.94, grayscale=True)
        foundConnectionError = py.locateCenterOnScreen(connectionError, region=(678, 444, 1221-678, 606-444), confidence=0.94, grayscale=True)

        if foundCaptainCleared != None:
            time.sleep(2)
            py.click(953, 660)
            print("Clicked Captain Cleared button.")

        if foundAnotherUser != None:
            time.sleep(2)
            py.click(953, 660)
            print("Clicked another user has taken this ship button.")

        if foundReload or foundReconnect != None:
            time.sleep(120)
            py.click(950, 670)
            print("Clicked reload/reconnect button.")

        if foundConnectionError != None:
            time.sleep(2)
            py.click(click_ok)
            print("Clicked ok on a connection error button.")

def click_galaxy():
    for i in range(3,0,-1):
        print(f"Clicking Galaxy in... {i}", end="\r", flush=True)
        time.sleep(1)
    galaxy_button = py.locateCenterOnScreen(galaxy, region=(1763,806,1913,1029), confidence=0.85)
    if galaxy_button != None:
        py.click(galaxy_button)

def click_ok():
    py.click(948, 666)

def keep_looking(log):
    py.moveTo(1715,1000,0.1)
    time.sleep(0.01)
    avoidLog(log)
    py.click()
    time.sleep(2)   

def avoidLog(log):
    #name = sliced_name.split("\\")[-1]
    skipTime = time.strftime("%d.%m.%Y - %H.%M.%S")
    # Print Avoided Details to terminal 
    avoidLog = open('.Ships Avoided.txt', 'a')
    avoidLog.write(log + " - " + skipTime)
    avoidLog.write("\n")
    avoidLog.close()
    time.sleep(2)

def attackLog():
    attackTime = time.strftime("%d.%m.%Y - %H.%M.%S")
	# Print attack details to terminal 
    print("Found something to attack at: " + str(attackTime))
    avoidLog = open('.Ships Attacked.txt', 'a')
    avoidLog.write("Found something to attack at: " + str(attackTime))
    avoidLog.write("\n")
    avoidLog.close()
    shipAttackedScreenshot()

def shipAttackedScreenshot():
    shipAttackedScreenshot = py.screenshot(region=(730,34,1214-748,128-34))
    save_path = r"C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\attackedShips"
    shipAttackedNumber = time.strftime("%d.%m.%Y-%H.%M.%S")
    completeName = os.path.join(save_path, str(shipAttackedNumber)+".png")
    shipAttackedScreenshot.save(completeName)
    
def moveScreenshot(new_directory):
    folder_path = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\attackedShips'
    file_type = '\*'
    file_path = glob.glob(folder_path + file_type)
    newest_file = max(file_path, key=os.path.getctime)

    sliced_file_name = newest_file.split("\\")[-1]
    sliced_destiation_path_name = new_directory.split("\\")[-1]

    if path.exists(newest_file):
         # Set the directory path where the file will be moved
        destination_path = new_directory
        shutil.move(newest_file, destination_path)
        print("%s has been moved to the location, %s" %(sliced_file_name, sliced_destiation_path_name))
    else:
        # Print the message if the file not exists
        print("Unable to move file.")

def exit():
    while True:
        foundVictory = py.locateCenterOnScreen(victory_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True) 
        if foundVictory != None:
            moveScreenshot(victory_directory)
            x = foundVictory[0]  
            y = foundVictory[1]
            for i in range(10,0,-1):
                print(f"Exiting in... {i}", end="\r", flush=True)
                time.sleep(1)
            py.click(x, y+200, clicks=10)
            time.sleep(3)

        foundDefeat = py.locateCenterOnScreen(defeat_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True)
        if foundDefeat != None:
            moveScreenshot(defeat_directory)
            x = foundDefeat[0]  
            y = foundDefeat[1]
            for i in range(10,0,-1):
                print(f"Exiting in... {i}", end="\r", flush=True)
                time.time.sleep(1)
            py.click(x, y+200, clicks=10)
            time.sleep(3)
        
        foundTimeout = py.locateCenterOnScreen(timeout_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True)
        if foundTimeout != None:
            moveScreenshot(timeout_directory)
            x = foundTimeout[0]  
            y = foundTimeout[1]
            for i in range(10,0,-1):
                print(f"Exiting in... {i}", end="\r", flush=True)
                time.time.sleep(1)
            py.click(x, y+200, clicks=10)
            time.sleep(3)

        foundEscape = py.locateCenterOnScreen(escape_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True)
        if foundEscape != None:
            moveScreenshot(defeat_directory)
            x = defeat_directory[0]  
            y = defeat_directory[1]
            for i in range(10,0,-1):
                print(f"Exiting in... {i}", end="\r", flush=True)
                time.time.sleep(1)
            py.click(x, y+200, clicks=10)            
            time.sleep(3)

def ShipDamage():
    for z in range (0, 10):
        sD = py.locateOnScreen(shipDamaged, region=(819,394,1113,483), confidence=0.92)
        if sD != None:
            py.click(yes)
            break

def closeWindows():
    while True:
        foundLeague = py.locateCenterOnScreen(league_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundProfile = py.locateCenterOnScreen(profile_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundFleet = py.locateCenterOnScreen(fleet_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundLadder = py.locateCenterOnScreen(ladder_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundBank = py.locateCenterOnScreen(bank_image, region=(1700, 38, 1860-1700, 38-99), confidence=0.94, grayscale=True) 
        foundShop = py.locateCenterOnScreen(shop_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True)  

        if foundLeague != None:
            time.sleep(2)
            py.click(1797, 134)
            print("League closed")
            
        if foundProfile != None:
            time.sleep(2)
            py.click(1797, 134)
            print("Profile closed")

        if foundFleet != None:
            time.sleep(2)
            py.click(1797, 134)
            print("Fleet closed")

        if foundLadder != None:
            time.sleep(2)
            py.click(1797, 134)
            print("Ladder closed")

        if foundShop != None:
            time.sleep(2)
            py.click(1797, 134)
            print("Shop closed")

        if foundBank != None:
            time.sleep(2)
            py.click(1886, 61)
            print("Bank closed")

def main():
    while True:
        if refit_check():
            ammo_reload()
            time.sleep(1)
            repair(yes)
            time.sleep(1)
            levelup(level_icon, level_y_0, level_y_1, level_x_0, level_x_1, level_x_adjustment, level_y_adjustment)
            time.sleep(1)
            buy_things()
            time.sleep(1)
            click_galaxy()   
            
class VideoCaptureThread(threading.Thread):
    def __init__(self, result_queue: queue.Queue) -> None:
        super().__init__()
        self.exit_signal = threading.Event()
        self.result_queue = result_queue

    def run(self) -> None:
        while not self.exit_signal.wait(0.05):
            try:
                result = videoLoop()
                self.result_queue.put(result)
            except Exception as exc:
                print(f"Failed capture: {exc}")

def detection():
    result_queue = queue.Queue()
    thread = VideoCaptureThread(result_queue=result_queue)
    thread.start()
    
    while True:   
        ships_to_avoid = loadImages(avoid)   
        # check if ready to run detection
        foundAttack = py.locateCenterOnScreen(attack_img, region=(1283, 935, 1553-1283, 1022-935), confidence=0.94, grayscale=True)
        if foundAttack != None:
            # load images to detect 
            
            prepare_objectDetection()
            print("Starting evasive maneuvers!")
            if shipDetection(ships_to_avoid):
                time.sleep(1)
                continue
            else:
                attack()              

def buy_things():
    buy(gas, currency_gas_location, item='Scratchy', y_offset=0)
    #buy(minerals, currency_min_location, item='Scrap',y_offset=-81)

def buy(rss, currency_location, item, y_offset):
    ready = py.locateCenterOnScreen(rss, region=(0, 236, 95-0, 452-236),confidence=0.94, grayscale=True)
    if ready != None:
        py.click(1878, 56)                      # click chat icon
        time.sleep(1)
        py.click(608, 226)                      # click market 
        time.sleep(1)
        py.click(1752, 330)                     # click search
        time.sleep(1)
        py.click(135, 1005)                     # click text input bar
        time.sleep(1)
        keyboard.type(item)
        time.sleep(2)
        py.click(1729, 932 + y_offset)          # select item
        time.sleep(2)
        py.click(419, 322)                      # click currency 
        time.sleep(2)
        py.click(currency_location)             # click gas
        time.sleep(3)
        py.click(1684, 994)                     # buy item
        time.sleep(2)
        py.click(1096, 581)                     # confirm purchase 
        time.sleep(1)
        py.click(1796, 140)                     # close window
        time.sleep(3)

    
#######################################
########## MAIN BOT SCRIPT ############
#######################################

# initialize the WindowCapture class
# left blank to capture the whole screen
app_window = WindowCapture()

for i in range(3,0,-1):
    print(f"Starting Bot in... {i}", end="\r", flush=True)
    time.sleep(1)

t1 = Thread(name='main', target=main)                   # refit, ammo, repair, levelup: no lock, no lock, no lock, lock
t2 = Thread(name='closeWindows', target=closeWindows)   # no lock  
t3 = Thread(name='exit', target=exit)                   # no lock
t4 = Thread(name='re-attack', target=click_random)         # no lock
t5 = Thread(name='pvp', target=pvp_check)               # no lock  

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

if __name__ == "__main__":
    detection()                                         # lock

