# Move the Robot to Desired Waypoint

Exercise how to make an action file for waypoint movement robot

## Create an Action File
1. Create a new directory for action
    - `cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/am_action_move_to`
    - `mkdir action`
    - `cd action`
    - `touch Tujuan.action`

2. Create an Action definition
    ```sh
    # goal
    int64 target_tujuan
    ---
    # result
    int64 hasil_tujuan
    ---
    # feedback
    int64 feedback_tujuan
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
        Tujuan.action
    )

    generate_messages(
        DEPENDENCIES
        actionlib_msgs
        std_msgs
    )

    catkin_package(
        #  INCLUDE_DIRS include
        #  LIBRARIES am_action_move_to
        CATKIN_DEPENDS actionlib_msgs rospy std_msgs
        #  DEPENDS system_lib
    )
	```

4. Build the package
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`

5. Check the action definition
	- `$ cd ~/catkin_ws/`
	- `$ cd devel/include/am_action_move_to`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	TujuanActionFeedback.h
	TujuanActionGoal.h
	TujuanAction.h
	TujuanActionResult.h
	TujuanFeedback.h
	TujuanGoal.h
	TujuanResult.h
	```
	
	- `$ cd ~/catkin_ws/devel/share/am_action_move_to/msg`
	- `$ ls`
	- The result will show up 7 new file
	```sh
	TujuanActionFeedback.msg
	TujuanActionGoal.msg
	TujuanAction.msg
	TujuanActionResult.msg
	TujuanFeedback.msg
	TujuanGoal.msg
	TujuanResult.msg
	```
	
	- How to check definition action
		- `$ cat TujuanActionFeedback.msg`
		- `$ cat TujuanActionGoal.msg`
		- `$ cat TujuanAction.msg`
		- `$ cat TujuanActionResult.msg`
		- `$ cat TujuanFeedback.msg`
		- `$ cat TujuanGoal.msg`
		- `$ cat TujuanResult.msg`

