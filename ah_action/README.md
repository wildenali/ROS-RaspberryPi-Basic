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
6. Build the project
	- Open a new terminal
	- `$ . ~/catkin_ws/devel/setup.bash`
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
7. Creata a `Action node` file called `ah_action_server.py`
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ah_action/src`
	- `$ touch ah_action_server.py`
	- `$ chmod +x ah_action_server.py`	change the permissions, to check type `$ ls -la`
8. Edit the `ah_action_server.py` file like below
	```sh
	#!/usr/bin/env python

	import rospy
	import time
	import actionlib	# import ini untuk menggunakan SimplaActionServer class
	from ah_action.msg import TimerAction, TimerGoal, TimerResult

	def doTimer(goal):	# fungsi program timer, fungsi ini dibuat untuk menghitung berapa lama waktu ketika server menerima pesan goal yg dikirim oleh client
		start_time = time.time()
		time.sleep(goal.time_to_wait.to_sec())
		result = TimerResult()
		result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)		# ini menghitung berapa lamanya
		result.updates_sent = 0
		server.set_succeeded(result)

	rospy.init_node('timer_action_server')
	server = actionlib.SimpleActionServer('timer', TimerAction, doTimer, False)
	server.start()
	rospy.spin()
	```
9. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/ah_action_server.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
10. Build the node
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`

11. Creata a `Client action node` file called `ah_action_client.py`
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ah_action/src`
	- `$ touch ah_action_client.py`
	- `$ chmod +x ah_action_client.py`	change the permissions, to check type `$ ls -la`
12. Edit the `ah_action_client.py` file like below
	```sh
	#!/usr/bin/env python

	import rospy
	import actionlib
	from ah_action.msg import TimerAction, TimerGoal, TimerResult

	rospy.init_node('timer_action_client')		# menamai node
	client = actionlib.SimpleActionClient('timer', TimerAction)		# menghubungkan ke server yg namanya timer
	client.wait_for_server()		# tunggu konek ke server

	goal = TimerGoal()
	goal.time_to_wait = rospy.Duration.from_sec(5.0)	# setting waktu berapa lama waktu yg ditunggu si client, yg akan di kirim ke server
	client.send_goal(goal)		# kirim data ke server
	client.wait_for_result()	# tunggu hasilnya
	print('Time elapsed: %f' %(client.get_result().time_elapsed.to_sec()))	
	```
13. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/ah_action_server.py
			src/ah_action_client.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
14. Build the node
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
15. Run package
	- `$ roscore`
	- Open a new terminal and type `$ rosrun ah_action_server.py`
	- Open a new terminal and type `$ rosrun ah_action_client.py`
