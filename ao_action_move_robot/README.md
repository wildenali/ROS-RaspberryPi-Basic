# How Far the Robot Move

[Action lib msg](http://docs.ros.org/en/kinetic/api/actionlib_msgs/html/msg/GoalStatus.html)

Debug Action using rqt
`$ rqt_graph`
uncentang Action label on rqt graph

# a_move_robot_server.py a_move_robot_client.py
How to use a basic Action Client Server
1. Create a new directory for action
    - `cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ao_action_move_robot`
    - `mkdir action`
    - `cd action`
    - `touch MoveRobot.action`

2. Create an Action definition
	```sh
	#goal
	int64 position	# m
	int64 velocity	# m/s
	---
	#result
	int64 position
	string message
	---
	#feedback
	int64 current_position
	```

3. Edit the package.xml
	```sh
	<buildtool_depend>catkin</buildtool_depend>

	<build_depend>actionlib_msgs</build_depend>
	<build_depend>rospy</build_depend>
	<build_depend>std_msgs</build_depend>

	<build_export_depend>actionlib_msgs</build_export_depend>
	<build_export_depend>rospy</build_export_depend>
	<build_export_depend>std_msgs</build_export_depend>

	<exec_depend>actionlib_msgs</exec_depend>
	<exec_depend>rospy</exec_depend>
	<exec_depend>std_msgs</exec_depend>
	<exec_depend>message_generation</exec_depend>
	```

4. Make sure the python script get installed properly and use the right python interpreter. Open CMakelist.txt file and add some code like below
	```sh
	find_package(catkin REQUIRED COMPONENTS
        actionlib_msgs
        rospy
        std_msgs
    )

    add_action_files(
        FILES
        CountUntil.action
    )

    generate_messages(
        DEPENDENCIES
        actionlib_msgs
        std_msgs
    )

    catkin_package(
        #  INCLUDE_DIRS include
        #  LIBRARIES an_action_count_until
        CATKIN_DEPENDS actionlib_msgs rospy std_msgs
        #  DEPENDS system_lib
    )
	```

5. Build the package
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`

6. Check the action definition
	- `$ cd ~/catkin_ws/`
	- `$ cd devel/include/ao_action_move_robot`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	MoveRobotActionFeedback.h
	MoveRobotActionGoal.h
	MoveRobotAction.h
	MoveRobotActionResult.h
	MoveRobotFeedback.h
	MoveRobotGoal.h
	MoveRobotResult.h
	```
	
	- `$ cd ~/catkin_ws/devel/share/ao_action_move_robot/msg`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	MoveRobotActionFeedback.msg
	MoveRobotActionGoal.msg
	MoveRobotAction.msg
	MoveRobotActionResult.msg
	MoveRobotFeedback.msg
	MoveRobotGoal.msg
	MoveRobotResult.msg
	```
	
	- How to check definition action
	`$ cat MoveRobotActionFeedback.msg`
	`$ cat MoveRobotActionGoal.msg`
	`$ cat MoveRobotAction.msg`
	`$ cat MoveRobotActionResult.msg`
	`$ cat MoveRobotFeedback.msg`
	`$ cat MoveRobotGoal.msg`
	`$ cat MoveRobotResult.msg`

7. Create a server file
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ao_action_move_robot/src`
	- `$ touch a_move_robot_server.py`
	- `$ chmod +x a_move_robot_server.py`
	- Make some code

8. Open CMakelist.txt file and add some code like below
	````sh
	catkin_install_python(PROGRAMS
		src/a_move_robot_server.py
		DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
	)
	```

9. Build the Server File
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`

10. Run the Server FIle
	- `$ roscore`
	- Open a new terminal
	- `$ catkin_make`
	- `$ rosrun ao_action_move_robot a_move_robot_server.py`

11. Check the rosnode and rostopic
	- `$ rosnode list`
	- `$ rostopic list`
	
12. Create a client file for action
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ao_action_move_robot/src`
	- `$ touch a_move_robot_client.py`
	- `$ chmod +x a_move_robot_client.py`
	- Make some code

13. Open CMakelist.txt file and add some code like below
	````sh
	catkin_install_python(PROGRAMS
		src/a_move_robot_client.py
		DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
	)
	```

14. Build the Server File
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`

15. Run the Client File
	- `$ roscore`
	- Open a new terminal
	- `$ catkin_make`
	- `$ rosrun ao_action_move_robot a_move_robot_client.py`

16. Check the rosnode and rostopic
	- `$ rosnode list`
	- `$ rostopic list`
	
17. Run Server and Client Action
	- `$ roscore`
	- `$ rosrun ao_action_move_robot a_move_robot_server.py`
	- `$ rosrun ao_action_move_robot a_move_robot_client.py`

