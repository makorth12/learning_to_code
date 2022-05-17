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
import subprocess
import psutil
import win32gui, win32con, win32ui
from pynput.keyboard import Controller
from os import path
from PIL import ImageGrab

# Change the working directory to the folder this script is in.
os.chdir(r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual')

avoid = glob.glob(r"C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\defeat\*.png")

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
scan = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\scan.png'

items = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\items.png'
item_repair = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\item_repair.png'

galaxy = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\galaxy.png'
health = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\health.png'
shipDamaged = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\shipDamaged.png'

chat_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\chat.png'
league_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\league_image.png'
profile_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\profile_image.png'
fleet_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\fleet_image.png'
ladder_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\ladder__image.png'
bank_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\bank_image.png'
captain_cleared_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\captaincleared_image.png'
shop_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\shop_image.png'
another_user_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\another_user_image.png'
captainLog = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\captainLog.png'
acquireBux = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\acquire.png'

reload = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\reload.png'
reconnect = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\reconnect.png'
connectionError = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\connectionError.png'
playAnyway = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\playAnyway.png'
click_to_escape_from_battle = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\click_to_escape_from_battle.png'
extendCheck = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\extendCheck.png'
lockedOut = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\lockedOut.png'
badgateway = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\badgateway.png'

collect = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\collect.png'
items = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\items.png'
checkBottomBar = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\checkBottomBar.png'
scratchy = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\scratchy.png'
plus = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\plus.png'
reachedSellingLimit = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\reachedSellingLimit.png'
addedToMarket = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\addedToMarket.png'


gas = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\rss\gas.png'
minerals = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\rss\mins.png'

currency_gas_location = 422, 545
currency_min_location = 412, 481

keyboard = Controller()

#level_icon = MatchTemplate_Vision(level)
#level_x_0, level_x_1 = 560, 860
#level_y_0, level_y_1 = 750, 870
#level_x_adjustment = 0
#level_y_adjustment = 0

yes = 1091, 606
no = 814, 614
chat = 1869, 64
inbox = 1029, 247
close_x = 1797, 134
sell = 1085, 662
backspace = 1191, 536
two = 869, 540
five = 894, 591
confirm = 1192, 764
ok = 956, 661

def refit_check():
    while True:
        res = 0
        foundRefit = py.locateCenterOnScreen(refit, region=(1843, 180, 1900-1843, 230-180), confidence=0.90, grayscale=True)
        if foundRefit != None:
            res = 1
            return res

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

def preProcessNeedle(image_list):
    needle_kp1_desc = []
    for i in image_list:
        name = i[1].split("\\")[-1]
        img = i[0]
        orb = cv.ORB_create(edgeThreshold=0, patchSize=32)
        keypoint_needle, descriptors_needle = orb.detectAndCompute(img, None)
        needle_kp1_desc.append((keypoint_needle, descriptors_needle, img, name))
    return needle_kp1_desc

def match_keypoints(counter, name, keypoints_needle, descriptors_needle, keypoint_haystack, min_match_count):
   
    orbHaystack = cv.ORB_create(edgeThreshold=0, patchSize=32, nfeatures=3000)
    keypoints_haystack, descriptors_haystack = orbHaystack.detectAndCompute(keypoint_haystack, None)

    FLANN_INDEX_LSH = 6
    index_params = dict(algorithm=FLANN_INDEX_LSH, table_number=6, key_size=12, multi_probe_level=1)
    search_params = dict(checks=50)

    try:
        flann = cv.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(descriptors_needle, descriptors_haystack, k=2)
    except cv.error:
            return None, None, [], []
        
    good = []
    points = []

    for pair in matches:
        if len(pair) == 2:
            if pair[0].distance < 0.7*pair[1].distance:
                good.append(pair[0])

    log = (str("Search Count: ") + str(counter) + str(" - ") + str("Searching for: ") + str(name) + ' - ' + '%03d keypoints matched - %03d' % (len(good), len(keypoints_needle)))
    print(log)

    if len(good) > min_match_count:
        for match in good:
            points.append(keypoints_haystack[match.trainIdx].pt)
    return keypoints_haystack, good, points, log

def centeroid(point_list):
    point_list = np.asarray(point_list, dtype=np.int32)
    length = point_list.shape[0]
    sum_x = np.sum(point_list[:, 0])
    sum_y = np.sum(point_list[:, 1])
    return [np.floor_divide(sum_x, length), np.floor_divide(sum_y, length)]

def draw_crosshairs(haystack_img, points):
    # these colors are actually BGR
    marker_color = (255, 255, 255)
    marker_type = cv.MARKER_CROSS
    for (center_x, center_y) in points:
        # draw the center point
        cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)
    return haystack_img

def get_haystack_image():
    w, h = 1920, 1080
    hwnd = None
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    img = img[...,:3]
    img = np.ascontiguousarray(img)
    return img

def videoLoop():
    try:
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
        return haystack
    except:
        time.sleep(1)
        print('Window not found.')

def shipDetection(needle_kp1_desc):
    counter = 0
    # start timer
    t0 = time.time()
    res = False

    # Object Detection
    for i, img in enumerate(needle_kp1_desc):
        counter += 1
        kp1 = img[0]
        descriptors_needle = img[1]
        needle_img = img[2]
        name = img[3]

        # get an updated image of the screen & crop it  
        keypoint_haystack = get_haystack_image()
        keypoint_haystack = keypoint_haystack[30:125, 800:1200]

        kp2, matches, match_points, ship_avoided = match_keypoints(counter, name, kp1, descriptors_needle, keypoint_haystack, min_match_count=70)     
        # display the matches
        match_image = cv.drawMatches(needle_img, kp1, keypoint_haystack, kp2, matches, None)
        cv.imshow('Keypoint Search', match_image)
        cv.moveWindow("Keypoint Search",1,-200)
        cv.waitKey(1)       

        if match_points:
            # find the center point of all the matched features
            width = needle_img.shape[1]
            center_point = centeroid(match_points)
            # account for the width of the needle image that appears on the left
            center_point[0] += width
            # drawn the found center point on the output image
            match_image = draw_crosshairs(match_image, [center_point])

            # display the processed image
            cv.imshow('Keypoint Search', match_image)
            cv.moveWindow("Keypoint Search",1,-200)
            cv.waitKey(1)       
            keep_looking()
            file_to_open = '.Ships Avoided.txt'
            avoidLog(file_to_open, ship_avoided)
            res = True
            break
        
    ts = time.time() - t0
    tdp = "{:.2f}".format(ts)
    print('Loop Time:',tdp)

    file_to_open = '.Loop Time.txt'
    avoidLog(file_to_open, tdp)
    return res

def prepare_objectDetection():
    print("Preparing Object Detection...")
    py.moveTo(921, 415)
    py.dragTo(921, 815, 0.3, button='left')
    print("Finished preparing Object Detection!")

def attack():
    py.moveTo(1415,1000,0.1)
    time.sleep(0.01)
    attackLog()
    py.click()
    time.sleep(3)

def click_galaxy():
    for i in range(3,0,-1):
        print(f"Clicking Galaxy in... {i}", end="\r", flush=True)
        time.sleep(1)
    galaxy_button = py.locateCenterOnScreen(galaxy, region=(1763,806,1913,1029), confidence=0.85)
    if galaxy_button != None:
        py.click(galaxy_button)

def click_ok():
    py.click(948, 666)

def keep_looking():
    py.click(1715,1000)

def avoidLog(file_to_open, data_to_log):
    Time = time.strftime("%d.%m.%Y - %H.%M.%S")
    avoidLog = open(file_to_open, 'a')
    avoidLog.write(data_to_log + " - " + Time)
    avoidLog.write("\n")
    avoidLog.close()

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
      
def ShipDamage():
    for z in range (0, 10):
        sD = py.locateOnScreen(shipDamaged, region=(819,394,1113,483), confidence=0.92)
        if sD != None:
            py.click(yes)
            break

def listeners():
    while True:
        foundLeague = py.locateCenterOnScreen(league_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundProfile = py.locateCenterOnScreen(profile_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundFleet = py.locateCenterOnScreen(fleet_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundLadder = py.locateCenterOnScreen(ladder_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundBank = py.locateCenterOnScreen(bank_image, region=(1700, 38, 1860-1700, 38-99), confidence=0.94, grayscale=True) 
        foundShop = py.locateCenterOnScreen(shop_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True)  
        foundCaptainLog = py.locateCenterOnScreen(captainLog, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True)  
        foundAcquireBux = py.locateCenterOnScreen(acquireBux, region=(717, 482, 858-717, 529-482), confidence=0.94, grayscale=True)  
        foundCaptainCleared = py.locateCenterOnScreen(captain_cleared_image, region=(661, 483, 1040-661, 591-483), confidence=0.94, grayscale=True)
        foundAnotherUser = py.locateCenterOnScreen(another_user_image, region=(678, 444, 1221-678, 606-444), confidence=0.94, grayscale=True)
        foundReload = py.locateCenterOnScreen(reload, region=(861, 653, 1022-861, 689-653), confidence=0.94, grayscale=True)
        foundReconnect = py.locateCenterOnScreen(reconnect, region=(678, 444, 1221-678, 606-444), confidence=0.94, grayscale=True)
        foundConnectionError = py.locateCenterOnScreen(connectionError, region=(678, 444, 1221-678, 606-444), confidence=0.94, grayscale=True)
        foundPVP = py.locateCenterOnScreen(pvp, region=(540, 874, 1381-540, 1033-874), confidence=0.94, grayscale=True)
        foundVictory = py.locateCenterOnScreen(victory_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True) 
        foundDefeat = py.locateCenterOnScreen(defeat_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True)
        foundTimeout = py.locateCenterOnScreen(timeout_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True)
        foundEscape = py.locateCenterOnScreen(escape_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True)
        playAnywayFound = py.locateCenterOnScreen(playAnyway, region=(523, 405, 1280-523, 790-405), confidence=0.94, grayscale=True)
        click_to_escape_from_battleFound = py.locateCenterOnScreen(click_to_escape_from_battle, region=(7, 32, 151-7, 86-32), confidence=0.90, grayscale=True)
        foundLockedOut = py.locateCenterOnScreen(lockedOut, region=(795, 399, 949-795, 466-399), confidence=0.94, grayscale=True)
        foundbadgateway = py.locateCenterOnScreen(badgateway, region=(691, 357, 1220-691, 583-357), confidence=0.94, grayscale=True)


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

        if foundCaptainLog != None:
            time.sleep(2)
            py.click(1886, 61)
            print("Captains log closed")

        if foundAcquireBux != None:
            time.sleep(2)
            py.click(no)
            print("Clicked no to acquire starbux!")
            
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
            py.click(948, 666)
            print("Clicked ok on a connection error button.")
        
        if foundPVP != None:
            time.sleep(1)
            print('Clicking PvP...')
            time.sleep(1)
            py.click(foundPVP)
            print('Clicked PvP!')
            time.sleep(1)
            ShipDamage()
            detection()

        if foundVictory != None:
            moveScreenshot(victory_directory)
            for i in range(5,0,-1):
                print(f"Exiting in... {i}", end="\r", flush=True)
                time.sleep(1)
            py.click(965, 541, clicks=10)
            time.sleep(3)

        if foundDefeat != None:
            moveScreenshot(defeat_directory)
            for i in range(5,0,-1):
                print(f"Exiting in... {i}", end="\r", flush=True)
                time.sleep(1)
            py.click(965, 541, clicks=10)
            time.sleep(3)
        
        if foundTimeout != None:
            moveScreenshot(timeout_directory)
            for i in range(5,0,-1):
                print(f"Exiting in... {i}", end="\r", flush=True)
                time.sleep(1)
            py.click(965, 541, clicks=10)
            time.sleep(3)

        if foundEscape != None:
            moveScreenshot(defeat_directory)
            for i in range(5,0,-1):
                print(f"Exiting in... {i}", end="\r", flush=True)
                time.sleep(1)
            py.click(965, 541, clicks=10)            
            time.sleep(3)

        if playAnywayFound != None:
            time.sleep (2)
            py.click(playAnywayFound)
            print("Clicked Steam Play Anyway!")

        if click_to_escape_from_battleFound != None:
            py.click(900, 45)
            print("Escaping!")
            time.sleep(1)
            py.click(1107, 589)
            print("Tried to Escaped!")
            time.sleep(10)

        if foundLockedOut != None:
            time.sleep(2)
            py.click(952, 585)
            print("Clicked Retry.")

        if foundbadgateway != None:
            time.sleep(1)
            py.click(ok)
            print("Clicked Bad Gateway ok.")

def detection():    
    while True:   
        ships_to_avoid = loadImages(avoid) 
        needle_kp1_desc = preProcessNeedle(ships_to_avoid)    
        # check if ready to run detection
        foundScan = py.locateCenterOnScreen(scan, region=(1612, 52, 1882-1612, 111-52), confidence=0.94, grayscale=True)
        if foundScan != None:
            # load images to detect 
            prepare_objectDetection()
            print("Starting evasive maneuvers!")
            if shipDetection(needle_kp1_desc):
                continue
            else:
                attack()
                return              

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

def start():
    subprocess.call([r"C:\Program Files (x86)\Steam\Steam.exe","-applaunch"," 378760","-fullscreen"])

def stop():
    subprocess.call(["taskkill","/F","/IM","Pixel Starships.exe"])

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return False
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return True;

def main():
    count = 0 
    t0 = time.time()
    t1 = 240
    while True:
        count = count + 1
        # if not running start 
        if checkIfProcessRunning('Pixel Starships.exe'):
            start()
            time.sleep(10)
            # maximise window
            py.click(1857, 32)

        if refit_check() == 1:
            ammo_reload()
            time.sleep(1)
            repair(yes)
            time.sleep(1)
            #levelup(level_icon, level_y_0, level_y_1, level_x_0, level_x_1, level_x_adjustment, level_y_adjustment)
            #time.sleep(1)
            buy_things()
            time.sleep(1)
            print("Sell Count: " + str(count))
            if count % 20 == True:
                collectSell()

        t2 = t0-t1
        print("Time Elapsed: " + str(t2))

        if (t0 := time.time()) >= t1:
            extend()
            t1 = t0 + 240
        else:
            click_galaxy()    

def extend():
    # if not selling start 
    chatFound = py.locateCenterOnScreen(chat_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
    if chatFound is None:
        # if not in a ship battle, stop
        extendCheckFound = py.locateCenterOnScreen(extendCheck, region=(854, 29, 1035-854, 74-29), confidence=0.94, grayscale=True) 
        if extendCheckFound == None:
            stop()

def collectSell():
    py.click(chat)
    time.sleep(1)
    py.click(inbox)
    time.sleep(1)

    for pos in py.locateAllOnScreen(collect, region=(1655, 272, 1824-1655, 992-272), confidence=0.94, grayscale=True):
        py.click(pos)
    time.sleep(1)
    py.click(ok)
    time.sleep(0.5)
    py.click(close_x)
    time.sleep(2)

    checkBottomBarFound = py.locateCenterOnScreen(checkBottomBar, region=(1146, 904, 1219-1146, 942-904), confidence=0.80, grayscale=True)
    # if drawer closed
    if checkBottomBarFound == None:
        itemMenuFound = py.locateCenterOnScreen(items, region=(159, 855, 268-159, 1031-855), confidence=0.80, grayscale=True)
        if itemMenuFound != None: py.click(itemMenuFound)
        time.sleep(1)
        itemMenuFound = py.locateCenterOnScreen(items, region=(159, 855, 268-159, 1031-855), confidence=0.80, grayscale=True)
        x = itemMenuFound[0]
        y = itemMenuFound[1]
        py.click(x+350, y)
        time.sleep(1)
        py.moveTo(548, 846)
        py.dragTo(548, 168, 0.3, button='left')
        time.sleep(1)
        py.moveTo(500, 621)
        py.dragTo(500, 685, 0.8, button='left')
        time.sleep(1)
        py.click(500,635)
        scratchyFound = py.locateCenterOnScreen(scratchy, region=(0, 938, 100-0, 1021,938), confidence=0.80, grayscale=True)
        py.click(scratchyFound)
        time.sleep(0.5)
        py.click(sell)    
        time.sleep(0.5)
        py.click(backspace)
        time.sleep(0.5)
        py.click(two)
        time.sleep(0.5)
        for x in range(19): 
            plusFound = py.locateCenterOnScreen(plus, region=(1036, 304, 1100-1036, 357-304), confidence=0.92, grayscale=True)
            py.click(plusFound)
        py.click(confirm)
        time.sleep(0.5)
        py.click(yes)
        time.sleep(1.5)
        reachedSellingLimitFound = py.locateCenterOnScreen(reachedSellingLimit, region=(651, 455, 983-651, 534-455), confidence=0.80, grayscale=True)
        if reachedSellingLimitFound != None: py.click(ok), py.click(1528, 228, clicks=2) 

        addedToMarketFound = py.locateCenterOnScreen(addedToMarket, region=(722, 479, 1199-722, 543-479), confidence=0.80, grayscale=True)
        if addedToMarketFound != None: py.click(ok), py.click(1528, 228, clicks=1) 

    # if drawer open    
    else: 
        itemMenuFound = py.locateCenterOnScreen(items, region=(159, 855, 268-159, 1031-855), confidence=0.80, grayscale=True)
        x = itemMenuFound[0]
        y = itemMenuFound[1]
        py.click(x+350, y)
        time.sleep(1)
        py.moveTo(548, 846)
        py.dragTo(548, 168, 0.3, button='left')
        time.sleep(1)
        py.moveTo(500, 621)
        py.dragTo(500, 685, 0.8, button='left')
        time.sleep(1)
        py.click(500,635)
        scratchyFound = py.locateCenterOnScreen(scratchy, region=(0, 938, 100-0, 1021-938), confidence=0.80, grayscale=True)
        py.click(scratchyFound)
        time.sleep(0.5)
        py.click(sell)
        time.sleep(0.5)
        py.click(backspace)
        time.sleep(0.5)
        py.click(two)
        time.sleep(0.5)
        for x in range(19): 
            plusFound = py.locateCenterOnScreen(plus, region=(1036, 304, 1100-1036, 357-304), confidence=0.92, grayscale=True)
            py.click(plusFound)
        py.click(confirm)
        time.sleep(0.5)
        py.click(yes)
        time.sleep(1.5)
        reachedSellingLimitFound = py.locateCenterOnScreen(reachedSellingLimit, region=(651, 455, 983-651, 534-455), confidence=0.80, grayscale=True)
        if reachedSellingLimitFound != None: py.click(ok), py.click(1528, 228, clicks=2) 

        addedToMarketFound = py.locateCenterOnScreen(addedToMarket, region=(722, 479, 1199-722, 543-479), confidence=0.80, grayscale=True)
        if addedToMarketFound != None: py.click(ok), py.click(1528, 228, clicks=1) 

#######################################
########## MAIN BOT SCRIPT ############
#######################################

for i in range(3,0,-1):
    print(f"Starting Bot in... {i}", end="\r", flush=True)
    time.sleep(1)

t1 = threading.Thread(name='closeWindows', target=listeners)                     
t2 = threading.Thread(name='main', target=main)                            # levelup: lock

t1.start()
t2.start()








