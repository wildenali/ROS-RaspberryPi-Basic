
# Move the Robot to Desired Waypoint

# a_count_until_client.py a_count_until_server.py
How to use a basic Action Client Server
1. Create a new directory for action
    - `cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until`
    - `mkdir action`
    - `cd action`
    - `touch CountUntil.action`

2. Create an Action definition
	```sh
	#goal
	int64 max_number
	float64 wait_duration
	---
	#result
	int64 count
	---
	#feedback
	float64 percentage
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
	- `$ cd devel/include/an_action_count_until`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	CountUntilActionFeedback.h
	CountUntilActionGoal.h
	CountUntilAction.h
	CountUntilActionResult.h
	CountUntilFeedback.h
	CountUntilGoal.h
	CountUntilResult.h
	```
	
	- `$ cd ~/catkin_ws/devel/share/an_action_count_until/msg`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	CountUntilActionFeedback.msg
	CountUntilActionGoal.msg
	CountUntilAction.msg
	CountUntilActionResult.msg
	CountUntilFeedback.msg
	CountUntilGoal.msg
	CountUntilResult.msg
	```
	
	- How to check definition action
	`$ cat CountUntilActionFeedback.msg`
	`$ cat CountUntilActionGoal.msg`
	`$ cat CountUntilAction.msg`
	`$ cat CountUntilActionResult.msg`
	`$ cat CountUntilFeedback.msg`
	`$ cat CountUntilGoal.msg`
	`$ cat CountUntilResult.msg`

7. Create a server file
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until/src`
	- `$ touch a_count_until_server.py`
	- `$ chmod +x a_count_until_server.py`
	- Make some code

8. Open CMakelist.txt file and add some code like below
	````sh
	catkin_install_python(PROGRAMS
		src/a_count_until_server.py
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
	- `$ rosrun an_action_count_until a_count_until_server.py`

11. Check the rosnode and rostopic
	- `$ rosnode list`
	- `$ rostopic list`
	
12. Create a client file for action
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until/src`
	- `$ touch a_count_until_client.py`
	- `$ chmod +x a_count_until_client.py`
	- Make some code

13. Open CMakelist.txt file and add some code like below
	````sh
	catkin_install_python(PROGRAMS
		src/a_count_until_client.py
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
	- `$ rosrun an_action_count_until a_count_until_client.py`

16. Check the rosnode and rostopic
	- `$ rosnode list`
	- `$ rostopic list`
	
17. Run Server and Client Action
	- `$ roscore`
	- `$ rosrun an_action_count_until a_count_until_server.py`
	- `$ rosrun an_action_count_until a_count_until_client.py`


# b_count_until_client_async.py b_count_until_server_async.py
How to use a basic Action Client Server
note: step 1 until 6 is same like above tutorial (a)
1. Create a new directory for action
    - `cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until`
    - `mkdir action`
    - `cd action`
    - `touch CountUntilAsync.action`

2. Create an Action definition
	```sh
	#goal
	int64 max_number
	float64 wait_duration
	---
	#result
	int64 count
	---
	#feedback
	float64 percentage
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
        CountUntilAsync.action
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
	- `$ cd devel/include/an_action_count_until`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	CountUntilAsyncActionFeedback.h
	CountUntilAsyncActionGoal.h
	CountUntilAsyncAction.h
	CountUntilAsyncActionResult.h
	CountUntilAsyncFeedback.h
	CountUntilAsyncGoal.h
	CountUntilAsyncResult.h
	```
	
	- `$ cd ~/catkin_ws/devel/share/an_action_count_until/msg`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	CountUntilAsyncActionFeedback.msg
	CountUntilAsyncActionGoal.msg
	CountUntilAsyncAction.msg
	CountUntilAsyncActionResult.msg
	CountUntilAsyncFeedback.msg
	CountUntilAsyncGoal.msg
	CountUntilAsyncResult.msg
	```
	
	- How to check definition action
	`$ cat CountUntilAsyncActionFeedback.msg`
	`$ cat CountUntilAsyncActionGoal.msg`
	`$ cat CountUntilAsyncAction.msg`
	`$ cat CountUntilAsyncActionResult.msg`
	`$ cat CountUntilAsyncFeedback.msg`
	`$ cat CountUntilAsyncGoal.msg`
	`$ cat CountUntilAsyncResult.msg`

7. Create a server file
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until/src`
	- `$ touch b_count_until_server_async.py`
	- `$ chmod +x b_count_until_server_async.py`
	- Make some code

8. Open CMakelist.txt file and add some code like below
	````sh
	catkin_install_python(PROGRAMS
		src/b_count_until_server_async.py
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
	- `$ rosrun an_action_count_until b_count_until_server_async.py`

11. Check the rosnode and rostopic
	- `$ rosnode list`
	- `$ rostopic list`
	
12. Create a client file for action
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until/src`
	- `$ touch b_count_until_client_async.py`
	- `$ chmod +x b_count_until_client_async.py`
	- Make some code

13. Open CMakelist.txt file and add some code like below
	````sh
	catkin_install_python(PROGRAMS
		src/b_count_until_client_async.py
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
	- `$ rosrun an_action_count_until b_count_until_client_async.py`

16. Check the rosnode and rostopic
	- `$ rosnode list`
	- `$ rostopic list`
	
17. Run Server and Client Action
	- `$ roscore`
	- `$ rosrun an_action_count_until b_count_until_server_async.py`
	- `$ rosrun an_action_count_until b_count_until_client_async.py`

# c_count_until_server_feedback.py c_count_until_client_feedback.py 
How to use a basic Action Client Server
note: step 1 until 6 is same like above tutorial (a or b)
1. Create a new directory for action
    - `cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until`
    - `mkdir action`
    - `cd action`
    - `touch CountUntilAsync.action`

2. Create an Action definition
	```sh
	#goal
	int64 max_number
	float64 wait_duration
	---
	#result
	int64 count
	---
	#feedback
	float64 percentage
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
        CountUntilAsync.action
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
	- `$ cd devel/include/an_action_count_until`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	CountUntilAsyncActionFeedback.h
	CountUntilAsyncActionGoal.h
	CountUntilAsyncAction.h
	CountUntilAsyncActionResult.h
	CountUntilAsyncFeedback.h
	CountUntilAsyncGoal.h
	CountUntilAsyncResult.h
	```
	
	- `$ cd ~/catkin_ws/devel/share/an_action_count_until/msg`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	CountUntilAsyncActionFeedback.msg
	CountUntilAsyncActionGoal.msg
	CountUntilAsyncAction.msg
	CountUntilAsyncActionResult.msg
	CountUntilAsyncFeedback.msg
	CountUntilAsyncGoal.msg
	CountUntilAsyncResult.msg
	```
	
	- How to check definition action
	`$ cat CountUntilAsyncActionFeedback.msg`
	`$ cat CountUntilAsyncActionGoal.msg`
	`$ cat CountUntilAsyncAction.msg`
	`$ cat CountUntilAsyncActionResult.msg`
	`$ cat CountUntilAsyncFeedback.msg`
	`$ cat CountUntilAsyncGoal.msg`
	`$ cat CountUntilAsyncResult.msg`

7. Create a server file
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until/src`
	- `$ touch c_count_until_server_feedback.py`
	- `$ chmod +x c_count_until_server_feedback.py`
	- Make some code

8. Open CMakelist.txt file and add some code like below
	````sh
	catkin_install_python(PROGRAMS
		src/c_count_until_server_feedback.py
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
	- `$ rosrun an_action_count_until c_count_until_server_feedback.py`

11. Check the rosnode and rostopic
	- `$ rosnode list`
	- `$ rostopic list`
	
12. Create a client file for action
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until/src`
	- `$ touch c_count_until_client_feedback.py`
	- `$ chmod +x c_count_until_client_feedback.py`
	- Make some code

13. Open CMakelist.txt file and add some code like below
	````sh
	catkin_install_python(PROGRAMS
		src/c_count_until_client_feedback.py
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
	- `$ rosrun an_action_count_until c_count_until_client_feedback.py`

16. Check the feedback
	- `$ rosnode list`
	- `$ rostopic list`
	- `$ rostopic echo /count_until_feedback/feedback`

17. Run Server and Client Action
	- `$ roscore`
	- `$ rosrun an_action_count_until c_count_until_server_feedback.py`
	- `$ rostopic echo /count_until_feedback/feedback`
	- `$ rosrun an_action_count_until c_count_until_client_feedback.py`



# d_count_until_server_goal.py d_count_until_client_goal.py 
How to send goal status between SUCCEEDED or ABORTED
note: step 1 until 6 is same like above tutorial (a, b or)
1. Create a new directory for action
    - `cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until`
    - `mkdir action`
    - `cd action`
    - `touch CountUntilAsync.action`

2. Create an Action definition
	```sh
	#goal
	int64 max_number
	float64 wait_duration
	---
	#result
	int64 count
	---
	#feedback
	float64 percentage
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
        CountUntilAsync.action
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
	- `$ cd devel/include/an_action_count_until`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	CountUntilAsyncActionFeedback.h
	CountUntilAsyncActionGoal.h
	CountUntilAsyncAction.h
	CountUntilAsyncActionResult.h
	CountUntilAsyncFeedback.h
	CountUntilAsyncGoal.h
	CountUntilAsyncResult.h
	```
	
	- `$ cd ~/catkin_ws/devel/share/an_action_count_until/msg`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	CountUntilAsyncActionFeedback.msg
	CountUntilAsyncActionGoal.msg
	CountUntilAsyncAction.msg
	CountUntilAsyncActionResult.msg
	CountUntilAsyncFeedback.msg
	CountUntilAsyncGoal.msg
	CountUntilAsyncResult.msg
	```
	
	- How to check definition action
	`$ cat CountUntilAsyncActionFeedback.msg`
	`$ cat CountUntilAsyncActionGoal.msg`
	`$ cat CountUntilAsyncAction.msg`
	`$ cat CountUntilAsyncActionResult.msg`
	`$ cat CountUntilAsyncFeedback.msg`
	`$ cat CountUntilAsyncGoal.msg`
	`$ cat CountUntilAsyncResult.msg`

7. Create a server file
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until/src`
	- `$ touch d_count_until_server_goal.py`
	- `$ chmod +x d_count_until_server_goal.py`
	- Make some code

8. Open CMakelist.txt file and add some code like below
	````sh
	catkin_install_python(PROGRAMS
		src/d_count_until_server_goal.py
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
	- `$ rosrun an_action_count_until d_count_until_server_goal.py`

11. Check the rosnode and rostopic
	- `$ rosnode list`
	- `$ rostopic list`
	
12. Create a client file for action
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/an_action_count_until/src`
	- `$ touch d_count_until_client_goal.py`
	- `$ chmod +x d_count_until_client_goal.py`
	- Make some code

13. Open CMakelist.txt file and add some code like below
	````sh
	catkin_install_python(PROGRAMS
		src/d_count_until_client_goal.py
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
	- `$ rosrun an_action_count_until d_count_until_client_goal.py`

16. Check the feedback
	- `$ rosnode list`
	- `$ rostopic list`

17. Run Server and Client Action
	- `$ roscore`
	- `$ rosrun an_action_count_until d_count_until_server_goal.py`
	- `$ rosrun an_action_count_until d_count_until_client_goal.py`
