import time
import pyautogui as py


def closeWindows():

    league_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\league_image.jpg'
    profile_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\profile_image.jpg'
    fleet_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\fleet_image.jpg'
    ladder_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\ladder__image.jpg'
    bank_image = r'C:\Users\coyle\OneDrive\froggy-pirate-master\avoidShips\avoidShipActual\images\bank_image.jpg'

    while True:
        foundLeague = py.locateCenterOnScreen(league_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundProfile = py.locateCenterOnScreen(profile_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundFleet = py.locateCenterOnScreen(fleet_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundLadder = py.locateCenterOnScreen(ladder_image, region=(738, 70, 1198-738, 158-70), confidence=0.94, grayscale=True) 
        foundBank = py.locateCenterOnScreen(bank_image, region=(1700, 38, 1860-1700, 38-99), confidence=0.94, grayscale=True) 

        if foundLeague or foundProfile or foundFleet or foundLadder != None:
            py.click(1797, 134)

        if foundBank != None:
            py.click(1887, 65)

