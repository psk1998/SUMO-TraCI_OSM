# SUMO_TraCI
### This repository contains a Python Script, a SUMO configuration (.sumocfg) file and a zip file containing files generated in a sample run. 
On running the Python Script, you are asked to input any location name (better keep it specific like - New York City, Carnegie Mellon University, etc). This geographic location is converted into coordinates using geocoder library. Then using Selenium library, a map of the given location in .osm format is downloaded into your default downloads folder. This file is then moved into your working directory (for which you will have to change the variable 'destination' in the python script).\
After the map.osm file is moved to the working directory, the network from this map is extracted into .net.xml format. Using randomTrips.py, random routes are generated in the network. In the .sumocfg file, the network file, route file and output files are declared.\
Finally, in the Python Script, TraCI is used to simulate the .sumocfg file and the output is stored in .out.xml format file.\
For your convineance, all the files generated on a sample run are given in the zip file.
