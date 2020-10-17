# Publisher and Subscriber - Python
In this tutorial, we will learn how to create the service node which will receive two ints and return the sum.

References:
- [https://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29](https://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29)

1. Create a directory called `srv`
	- Open a terminal
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/af_service_and_client`
	- `$ mkdir srv`
	- `$ cd srv`
2. Create a srv file called `af_penjumlahan.srv`
	- `$ touch af_penjumlahan.srv`
3. Define a new msg in the ad_service.srv file like below
	```sh
	int64 a
	int64 b
	---
	int64 sum
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
		#   Service1.srv
		#   Service2.srv
			af_penjumlahan.srv
		)
		```
6. Build the project
	- Open a new terminal
	- `$ . ~/catkin_ws/devel/setup.bash`
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
7. How to use rossrv
	- `$ rossrv show af_service_and_client/af_penjumlahan` or
	- `$ rossrv show af_penjumlahan`
8. Creata a `SERVICE NODE` file called `af_server.py`
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/af_service_and_client/src`
	- `$ touch af_server.py`
	- `$ chmod +x af_server.py`	change the permissions, to check type `$ ls -la`
9. Edit the `af_server.py` file like below
	```sh
	#!/usr/bin/env python

	from af_service_and_client.srv import af_penjumlahan
	from af_service_and_client.srv import af_penjumlahanRequest
	from af_service_and_client.srv import af_penjumlahanResponse

	import rospy

	def handlePenjumlahan(rekuest):
		print(rekuest)
		print("Hasilnya adalah: %s + %s = %s" %(rekuest.a, rekuest.b, (rekuest.a + rekuest.b))
		return af_penjumlahanResponse(rekuest.a + rekuest.b)

	def penjumlahanServer():
		rospy.init_node('penjumlahan_server')
		s = rospy.Service('penjumlahan', af_penjumlahan, handlePenjumlahan)
		print("Udah siap nih server, Ayo jumlahin")
		rospy.spin()

	if __name__ == '__main__':
		penjumlahanServer()
	```
10. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/af_server.py
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
11. Build the node
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`
12. Run the node
	- `$ cd ~/catkin_ws/`
	- `$ roscore`
	- Open a new tab and type `$ rosrun af_service_and_client af_server.py`
	- Close the all terminal to stop it
