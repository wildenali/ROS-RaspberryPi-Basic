# Action

References:
- [https://wiki.ros.org/actionlib](https://wiki.ros.org/actionlib)

1. Create a directory called `action`
	- Open a terminal
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ah_action`
	- `$ mkdir action`
	- `$ cd action`
2. Create an action file called `Timer.action`
	- `$ touch Timer.action`
3. Define a new action in the Timer.action file like below
	```sh
	duration time_to_wait
	---
	duration time_elapsed
	uint32 updates_sent
	---
	duration time_elapsed
	duration time_remaining
	---
	```
4. Make sure these two lines are in it and uncommented the `message_generation` and `message_runtime` in the package.xml file
	- Open package.xml file
	- Add code for actionlib
		```sh
		<build_depend>message_generation</build_depend>
		<build_export_depend>message_generation</build_export_depend>
		
		<build_depend>actionlib_msgs</build_depend>
		<build_export_depend>actionlib_msgs</build_export_depend>
		<exec_depend>actionlib_msgs</exec_depend>
		```
5. Edit on the CMakelists.txt file to add ROS msg
	- Open CMakelists.txt
	- Edit on the `find_package` like below
		```sh
		find_package(catkin REQUIRED COMPONENTS
		  rospy
		  std_msgs
		  actionlib_msgs
		)
		```
	- Add Timer.action
		```sh
		add_action_files(
			DIRECTORY action
			FILES Timer.action
		)
		```
	- Add actionlib_msgs on the geneerate_messages
		```sh
		generate_messages(
			DEPENDENCIES
			std_msgs
			actionlib_msgs
		)
		```
	- Add actionlib_msgs on the catkin_package
		```sh
		catkin_package(
		#  INCLUDE_DIRS include
		#  LIBRARIES ah_action
		  CATKIN_DEPENDS rospy std_msgs actionlib_msgs
		#  DEPENDS system_lib
		)
		```
