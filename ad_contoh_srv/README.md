# ROS Service - rossrv
In this tutorial, we will learn how to create message file and how to configure it

References:
- [https://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv](https://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv)
- [https://roboticsbackend.com/what-is-a-ros-service](https://roboticsbackend.com/what-is-a-ros-message)

1. Create a directory called `srv`
	- Open a terminal
	- `$ cd ~/catkin/src/ROS-RaspberryPi-Basic/ad_contoh_srv`
	- `$ mkdir srv`
	- `$ cd srv`
2. Create a srv file called `ad_service.srv`
	- `$ touch ad_service.srv`
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
			ad_service.srv
		)
		```
6. Build the project
	- Open a new terminal
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
7. How to use rossrv
	- `$ rossrv show ad_contoh_srv/ad_service` or
	- `$ rossrv show ad_service`
