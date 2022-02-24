import cv2 as cv
import numpy as np
import os
import pyautogui as py
import glob
import time
import shutil
import pygetwindow
import close_windows
from windowcapture import WindowCapture
from vision import Vision
from time import sleep
from os import path
from PIL import ImageGrab

# Change the working directory to the folder this script is in.
os.chdir(r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual')

avoid = glob.glob(r"C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\defeat\*.png")

victory_directory = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\victory'
defeat_directory = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\defeat'
timeout_directory = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\timeout'

victory_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\victory.jpg'
defeat_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\defeat.jpg'
timeout_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\timeout.jpg'
escape_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\escape.jpg'

ammo = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\ammo.jpg'
level = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\arrow.jpg'
refit = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\shipReadyToRefitIcon.jpg'
pvp = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\pvp.jpg'

galaxy = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\galaxy.jpg'
health = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\health.jpg'
shipDamaged = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\shipDamaged.jpg'


# initialize the WindowCapture class
# left blank to capture the whole screen
app_window = WindowCapture()

# initialize the Vision class
ammo_icon = Vision(ammo)
ammo_x_0, ammo_x_1 = 1790, 1900
ammo_y_0, ammo_y_1 = 750, 800
ammo_x_adjustment = -1175
ammo_y_adjustment = -95

level_icon = Vision(level)
level_x_0, level_x_1 = 560, 860
level_y_0, level_y_1 = 750, 870
level_x_adjustment = 0
level_y_adjustment = 0

refit_icon = Vision(refit)
refit_x_0, refit_x_1 = 10, 130
refit_y_0, refit_y_1 = 150, 220
refit_x_adjustment = 0
refit_y_adjustment = 0

pvp_icon = Vision(pvp)
pvp_x_0, pvp_x_1 = 635, 1225
pvp_y_0, pvp_y_1 = 908, 1029
pvp_x_adjustment = 0
pvp_y_adjustment = 0

health_check_x = 535
health_check_y = 68

yes = 1091, 606

def pvp_check(object, y_0, y_1, x_0, x_1, x_adjustment, y_adjustment):
    for x in range (0, 50):
        haystack = app_window.get_haystack()
        location = haystack[y_0:y_1, x_0:x_1]
        img = object.find(location, 0.92, 'points1', 'PvP')
        if img:           
            x_coord = img[0][0] + x_0
            y_coord = img[0][1] + y_0
            print("Clicking PvP button...")
            sleep(1)
            py.click(x_coord, y_coord)
            sleep(1)
            print("Clicked PvP button!")
            sleep(3)
            break
        
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

def refit_check(object, y_0, y_1, x_0, x_1, x_adjustment, y_adjustment):
    for z in range (0, 10):
        haystack = app_window.get_haystack()
        location = haystack[y_0:y_1, x_0:x_1]
        img = object.find(location, 0.92, 'points1','Refit')
        if img:
            return True
        
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

def ammo_reload(object, y_0, y_1, x_0, x_1, x_adjustment, y_adjustment):
    for z in range (0, 10):
        haystack = app_window.get_haystack()
        location = haystack[y_0:y_1, x_0:x_1]
        img = object.find(location, 0.92, 'points1','ammo')
  
        if img:
            x_coord = img[0][0] + x_0
            y_coord = img[0][1] + y_0
            print("Reloading ship...")
            py.click(x_coord, y_coord)
            sleep(1)
            print("Ship reload complete!")
            py.click(x_coord + x_adjustment, y_coord + y_adjustment)
            sleep(3)
            break
        
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

def repair(pixel_x, pixel_y, yes_location):
    for z in range (0, 10):
        g = py.locateOnScreen(galaxy, region=(1771,918,1904,1029), confidence=0.92)
        h = py.locateOnScreen(health, region=(449,55,561,80), confidence=0.92)
        if g and h != None:
            r,g,b = py.pixel(pixel_x, pixel_y)
            if r == 16:
                print("Reparing ship...")
                py.click(pixel_x,pixel_y)
                sleep(1)
                py.click(yes_location)
                print("Ship repair complete!")
                sleep(3)
                break
        
def levelup(object, y_0, y_1, x_0, x_1, x_adjustment, y_adjustment):
    for z in range (0, 10):
        haystack = app_window.get_haystack()
        location = haystack[y_0:y_1, x_0:x_1]
        img = object.find(location, 0.92, 'points1','levelup')
       
        if img:
            x_coord = img[0][0] + x_0
            y_coord = img[0][1] + y_0
            print("Levelling up...")
            py.click(x_coord,y_coord)
            sleep(1)
            x, y = py.position()
            py.click(x+120, y+160)
            sleep(1)
            x, y = py.position()
            py.click(x,y+50)
            print("Levelled up!")

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

def loadImages(directory):
	# Intialise empty array
	image_list = []
	# Add images to array
	for i in directory:
		img = cv.imread(i, cv.IMREAD_REDUCED_GRAYSCALE_2)
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
    (width, height) = (haystack_img.width // 2, haystack_img.height // 2)
    haystack_img_resized = haystack_img.resize((width, height))
    crop = haystack_img_resized.crop((360,22,600,65))
    haystack_img_np = np.array(crop)
    haystack = cv.cvtColor(haystack_img_np, cv.COLOR_BGR2GRAY)
    cv.imshow("Ship Detection", haystack)
    cv.waitKey(1)
    return haystack

def shipDetection(image_list, threshold, haystack, a):
    # Object Detection
    for x in range (0, a):
        for i in image_list:
            cv.imshow("Ship Detection", haystack)
            cv.waitKey(1)
            needle_img = i[0]
            needle_name = i[1]
            sliced_name = needle_name.split("\\")[-1]
            result = cv.matchTemplate(haystack, needle_img, cv.TM_CCORR_NORMED)

            # Get the best match position
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            percentage_max_val = round(max_val*100, 2)

            # Define top left and bottom right and threshold
            (H, W) = i[0].shape[:2] 
            top_left = max_loc
            bottom_right = (top_left[0] + W, top_left[1] + H)

            # If something has been detected click keep looking code
            if max_val >= threshold:
                cv.rectangle(haystack, top_left, bottom_right, 255, 2)
                cv.imshow("Ship Detection", haystack)
                cv.waitKey(1)
                keep_looking(sliced_name, percentage_max_val)
                return True
        return False

def prepare_objectDetection():
    py.moveTo(921, 415)
    py.sleep(1)
    py.dragTo(921, 615, 1, button='left')

def attack():
    py.moveTo(1415,1000,0.1)
    py.sleep(0.01)
    attackLog()
    py.click()
    exit()

def click_galaxy():
    py.click(1807, 1010)

def keep_looking(sliced_name, percentage_max_val):
    py.moveTo(1715,1000,0.1)
    py.sleep(0.01)
    avoidLog(sliced_name, percentage_max_val)
    py.click()    

def avoidLog(sliced_name, percentage_max_val):
    name = sliced_name.split("\\")[-1]
    skipTime = time.strftime("%d.%m.%Y - %H.%M.%S")
    # Print Avoided Details to terminal
    print("Keep Looking - " + str(percentage_max_val) + "% sure we avoided: " + str(name) + " at: " + str(skipTime))   
    avoidLog = open('.Ships Avoided.txt', 'a')
    avoidLog.write("Keep Looking - Avoided: " + str(name) + " at: " + str(skipTime))
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
    shipAttackedScreenshot = py.screenshot(region=(748,34,1096-748,69-34))
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
                print(f"{i}", end="\r", flush=True)
                time.sleep(1)
            py.click(x, y+200, clicks=10)
            break

        foundDefeat = py.locateCenterOnScreen(defeat_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True)
        if foundDefeat != None:
            moveScreenshot(defeat_directory)
            x = foundDefeat[0]  
            y = foundDefeat[1]
            for i in range(10,0,-1):
                print(f"{i}", end="\r", flush=True)
                time.sleep(1)
            py.click(x, y+200, clicks=10)
            break

        foundTimeout = py.locateCenterOnScreen(timeout_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True)
        if foundTimeout != None:
            moveScreenshot(timeout_directory)
            x = foundTimeout[0]  
            y = foundTimeout[1]
            for i in range(10,0,-1):
                print(f"{i}", end="\r", flush=True)
                time.sleep(1)
            py.click(x, y+200, clicks=10)
            break

        foundEscape = py.locateCenterOnScreen(escape_image, region=(600, 213, 1245-600, 609-213), confidence=0.94, grayscale=True)
        if foundEscape != None:
            moveScreenshot(defeat_directory)
            x = defeat_directory[0]  
            y = defeat_directory[1]
            for i in range(10,0,-1):
                print(f"{i}", end="\r", flush=True)
                time.sleep(1)
            py.click(x, y+200, clicks=10)
            break

def sD():
    for z in range (0, 10):
        sD = py.locateOnScreen(shipDamaged, region=(819,394,1113,483), confidence=0.92)
        if sD != None:
            py.click(yes)
            break


#############################
###### MAIN BOT SCRIPT ######
#############################


close_windows.closeWindows

while True:
    if refit_check(refit_icon, refit_y_0, refit_y_1, refit_x_0, refit_x_1, refit_x_adjustment, refit_y_adjustment):
        ammo_reload(ammo_icon, ammo_y_0, ammo_y_1, ammo_x_0, ammo_x_1, ammo_x_adjustment, ammo_y_adjustment)
        repair(health_check_x, health_check_y, yes)
        levelup(level_icon, level_y_0, level_y_1, level_x_0, level_x_1, level_x_adjustment, level_y_adjustment)
        click_galaxy()
        pvp_check(pvp_icon, pvp_y_0, pvp_y_1, pvp_x_0, pvp_x_1, pvp_x_adjustment, pvp_y_adjustment)
        sD()
 

    # load images to detect 
    ships_to_avoid = loadImages(avoid)
    # load application window to detect on
    window = videoLoop()

    # Listener to check if attack! button displaying
    x, y = 1742, 979
    r,g,b = py.pixel(x, y)
    if b == 106:

        prepare_objectDetection()
        if shipDetection(ships_to_avoid, 0.92, window, 50):
            py.sleep(6)
            continue
        else:
            attack()
