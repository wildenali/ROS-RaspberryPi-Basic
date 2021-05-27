
# Move the Robot to Desired Waypoint

Exercise how to make an action file

## Create an Action File
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


## Edit the package.xml and CMakeLists.txt
1. Open package.xml file and add some code like below
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

2. Make sure the python script get installed properly and use the right python interpreter. Open CMakelist.txt file and add some code like below
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

4. Build the package
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`

5. Check the action definition
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
		- `$ cat CountUntilActionFeedback.msg`
		- `$ cat CountUntilActionGoal.msg`
		- `$ cat CountUntilAction.msg`
		- `$ cat CountUntilActionResult.msg`
		- `$ cat CountUntilFeedback.msg`
		- `$ cat CountUntilGoal.msg`
		- `$ cat CountUntilResult.msg`

