# ROS Launch
In this tutorial, we will learn how to create message file and how to configure it

References:
- [https://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv](https://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv)
- [https://roboticsbackend.com/what-is-a-ros-message](https://roboticsbackend.com/what-is-a-ros-message)

1. Create a directory called `msg`
	- Open a terminal
	- `$ cd ~/catkin/src/ROS-RaspberryPi-Basic/ac_contoh_msg`
	- `$ mkdir msg`
	- `$ cd msg`
2. Create a msg file called `Num.msg`
	- `$ touch Num.msg`
3. Define a new msg in the Num.msg file like below
	```sh
	string first_name
	string last_name
	uint8 age
	uint32 score
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
	- Export message runtime dependency
		```sh
		catkin_package(
		#  INCLUDE_DIRS include
		#  LIBRARIES ac_contoh_msg
			CATKIN_DEPENDS rospy std_msgs message_runtime
		#  DEPENDS system_lib
		)
		```
	- Add Num.msg
		```sh
		add_message_files(
		   FILES
		#   Message1.msg
		#   Message2.msg
			Num.msg
		)
		```
	- Call the generate_messages() function
		```sh
		generate_messages(
			DEPENDENCIES
			std_msgs
		)
		```
5. How to use rosmsg
	- Open a new terminal
	- `$ rosmsg show ac_contoh_msg/Num` or
	- `$ rosmsg show Num`
