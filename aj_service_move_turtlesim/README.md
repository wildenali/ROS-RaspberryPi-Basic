# Service and Client

Exercise how to run a turtlesim node and make it a Square move with input First Name and Last Name 
- First you have to run the turtlesim node
- Terminal command will run the project package and included the First and Last Name
- The server.py will run the server of project package and get First and Last Name from terminal command
- The client.py will get fullname from server and it will move the turtlesim

References:
- ROS Ultimate Guide to Beginners Guide Hands ON! from Muhammad Luqman Udemy Channel

## Create a Service file
1. Create a directory called `srv`
	- Open a terminal
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/aj_service_move_turtlesim`
	- `$ mkdir srv`
	- `$ cd srv`
2. Create a srv file called `new.srv`
	- `$ touch new.srv`
3. Define a new msg in the ad_service.srv file like below
	```sh
	string name1
	string name2
	---
	string fullname
	```
4. Make sure these two lines are in it and uncommented the `message_generation` and `message_runtime` in the package.xml file
	- Open package.xml file
	- Uncomment `<build_depend>message_generation</build_depend>`
	- Uncomment `<exec_depend>message_runtime</exec_depend>`
5. Edit on the CMakelists.txt file to add ROS msg
	- Open CMakelists.txt
	- Edit on the `find_package` like below
		```sh
		find_package(catkin REQUIRED COMPONENTS
		  rospy
		  std_msgs
		  message_generation
		)
		```
	- Add ad_service.srv
		```sh
		add_service_files(
			FILES
			new.srv
		)
		```
	- Edit on the `catkin_package`
	```sh
	catkin_package(
	#  INCLUDE_DIRS include
		LIBRARIES aj_service_move_turtlesim
		CATKIN_DEPENDS rospy std_msgs message_runtime
		DEPENDS system_lib
	)
	```
6. Build the project
	- Open a new terminal
	- `$ . ~/catkin_ws/devel/setup.bash`	# Opsional
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
7. How to use rossrv
	- `$ rossrv info aj_service_move_turtlesim/new.srv` or
	- `$ rossrv show aj_service_move_turtlesim/new` or
	- `$ rossrv show aj_service_move_turtlesim/new.srv` or
	- `$ rossrv show new.srv`

## Create a Server file
1. Creata a `SERVER NODE` file called `aj_server.py`
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/aj_service_move_turtlesim/src`
	- `$ touch aj_server.py`
	- `$ chmod +x aj_server.py`	change the permissions, to check type `$ ls -la`
2. Edit the `aj_server.py` file like below
	```sh
	#!/usr/bin/env python

	from aj_service_move_turtlesim.srv import *
	import rospy

	def concatinate_Name(req):
		print(req)
		return newResponse(req.name1 + req.name2)

	def security_Server():
		rospy.init_node('security')
		s = rospy.Service('name_confirmation', new, concatinate_Name)
		print("Udah siap nih server, Ayo cuus")
		rospy.spin()

	if __name__ == '__main__':
		security_Server()
	```
3. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/aj_server.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
	- Uncomment
		```sh
		generate_messages(
			DEPENDENCIES
			std_msgs
		)
		```
4. Build the node
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`
5. Run the node
	- `$ cd ~/catkin_ws/`
	- `$ roscore`
	- Open a new tab and type `$ rosrun aj_service_move_turtlesim aj_server.py`
6. Test rosservice call
	- Open a new terminal
	- `rosservice call /name_confirmation Wilden Ali`
	- `rosservice call /name_confirmation "name1: 'Wilden'
	name2: 'Ali'"`
	- Close the all terminal to stop them

## Create a Client file
1. Creata `CLIENT NODE` file called `aj_client.py`
	- Open a new terminal
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/aj_service_move_turtlesim`
	- `$ cd src`
	- `$ touch aj_client.py`
	- `$ chmod +x aj_client.py`	change the permissions, type `$ la -la` to check permissions status
2. Edit the `aj_client.py` file like below
	```sh
	#!/usr/bin/env python

	import sys
	import rospy
	from geometry_msgs.msg import Twist
	from aj_service_move_turtlesim.srv import *

	def concate_name_client(x, y):
		rospy.wait_for_service('name_confirmation')
		concat_name = rospy.ServiceProxy('name_confirmation', new)
		resp1 = concat_name(x, y)
		return resp1

	def useage():
		return "%s [x y]" %sys.argv[0]

	def security_Verifying():
		pub = rospy.Publisher('/turtle1/cmd_vel', Twist)
		rospy.sleep(1)
		r = rospy.Rate(5.0)
		while not rospy.is_shutdown():
			twist = Twist()
			twist.linear.x = 0.3
			for i in range(10):
				pub.publish(twist)
				r.sleep()
			
			twist = Twist()
			twist.angular.z = 1.57/2
			for i in range(10):
				pub.publish(twist)
				r.sleep()

	if __name__ == '__main__':
		rospy.init_node('move_after_security')
		if len(sys.argv) == 3:
			x = sys.argv[1]
			y = sys.argv[2]
		else:
			print(useage())
			sys.exit(1)
		
		result = concate_name_client(x, y)
		if (result.fullname) == "WildenAli":
			security_Verifying()
		else :
			print("Salah Orang")
	```
3. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/aj_server.py
			src/aj_client.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
4. Because we use Twist to move turtlesim_node , we need type the `geometry_msgs` in the package.xml file
	- Open package.xml file
	- Type `<build_depend>geometry_msgs</build_depend>`
	- Type `<exec_depend>geometry_msgs</exec_depend>`
5. Build the node
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
	- `$ source devel/setup.bash`
6. Run the node
	- `$ cd ~/catkin_ws`
	- `$ roscore`
	- Open a new tab and type `$ rosrun aj_service_move_turtlesim aj_server.py`
	- Open a new tab and type `$ rosrun turtlesim turtlesim_node`
	- Open a new tab and type `$ rosrun aj_service_move_turtlesim aj_client.py Wilden Ali`
