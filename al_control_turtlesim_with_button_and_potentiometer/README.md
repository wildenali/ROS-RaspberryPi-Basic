# Remote Control Real Mobile Robot
# BELUM SELESAI, pakai TCP error soalnya

Exercise how to control the turtlesim node with button and potentiometer in the nodemcu (esp8266) board 
- Nodemcu(esp8266) with button and potentiometer
- Arduino
- Electrical Wiring Diagram
- Mechanical Assembly
- Using turtlesim node

References:
- ROS Ultimate Guide to Beginners Guide Hands ON! from Muhammad Luqman Udemy Channel

## Create a Main file
1. Creata a main file called `remote_the_turtlesim.py`
	- `$ cd src`
	- `$ touch remote_the_turtlesim.py`
	- `$ chmod +x remote_the_turtlesim.py`	change the permissions
2. Edit the `remote_the_turtlesim.py` file like below
	```sh
	
	```
3. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/remote_the_turtlesim.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
4. Build the node
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`
5. Run the node
	- `$ cd ~/catkin_ws/`
	- `$ roscore`
	- Open a new tab and type `rosrun rosserial_python serial_node.py tcp`
	- Open a new tab and type `$ rosrun al_control_turtlesim_with_button_and_potentiometer remote_the_turtlesim.py`
	- Close the all terminal to stop it

## Install teleop_twist_keyboard
`sudo apt-get install ros-kinetic-teleop-twist-keyboard`

## Create a Arduino file to receive a message and move the robot
1. Create a arduino file called `send_to_ROS.ino`
2. Edit the `send_to_ROS.ino` file like following below
	```sh
	
	```
3. Upload the file to esp8266 (nodemcu or wemos)
4. Assembly the robot
5. Turn on the robot




sudo apt-get install ros-kinetic-rosserial-python
sudo apt-get install ros-kinetic-rosserial-arduino
