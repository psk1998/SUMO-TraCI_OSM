# Import all the necessary Libraries
import json
import urllib.request
from selenium import webdriver
import geocoder
import os, shutil
import time
import traci

# Input the name of the location
city = input('Place Name:')
# Geocoder to get the coordinates of the location
g = geocoder.osm(city)
coordinates = str(g.osm['y'])+str('/')+str(g.osm['x'])
coordinates_url = 'https://www.openstreetmap.org/export#map=16/'+coordinates

print('Beginning file download using Selenium Libraries.....')
print('Downloading the file from- '+coordinates_url)

# Automating the downloading process using Selenium
driver = webdriver.Chrome(executable_path=r'C:\Users\padis\Downloads\chromedriver.exe')
driver.get(coordinates_url)
xpath = '//*[@id="export_commit"]/div/input'
selector  = '#export_commit > div > input[type=submit]'
element = driver.find_elements_by_css_selector(selector)[0]
element.click()

print('OSM File Downloaded!')
# Gap so that the file gets downloaded properly
time.sleep(3)

# Source - Place where it is downloaded *YOU WILL HAVE TO EDIT THIS*
source = r"C:\Users\padis\Downloads\map.osm"
# Destination - Current Working Directory *YOU WILL HAVE TO EDIT THIS*
destination = r"C:\Users\padis\sumo_primer\third\map.osm"
shutil.move(source,destination)

# Use CMD commands to convert the OSM file to Network File
os.system('cmd /c "netconvert --osm map.osm -o map.net.xml"')
# Used CMD commands to generate Random trips
os.system('cmd /c "randomTrips.py -n  map.net.xml -r map.rou.xml -e500 -l"')

# Traci is used to run SUMO-GUI and simulate the Traffic Model
sumoBinary = "sumo-gui"
sumoCmd = [sumoBinary, "-c", "map.sumocfg",'--time-to-teleport','200']

traci.start(sumoCmd)
step = 0
while step < 500:
    traci.simulationStep()
    #print(traci.vehicle.getCO2Emission)
    step += 1
    time.sleep(0.01)

traci.close()
print('Done!')