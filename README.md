# ROS on Raspberry Pi

##### References
- [https://emanual.robotis.com/docs/en/platform/turtlebot3/raspberry_pi_3_setup/#raspberry-pi-3-setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/raspberry_pi_3_setup/#raspberry-pi-3-setup)
- [http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi)``

## `Install ROS`
- [http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi)

#### Install ROS Kinetic on Raspberry Pi Ubuntu Mate 16.04
```sh
$ sudo apt-get update
$ sudo apt-get upgrade
$ wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic_rp3.sh && chmod 755 ./install_ros_kinetic_rp3.sh && bash ./install_ros_kinetic_rp3.sh
$ sudo apt-get install ros-kinetic-rosserial-python ros-kinetic-tf
$ source /opt/ros/kinetic/setup.bash
$ cd ~/catkin_ws && catkin_make -j1
```

## `Creating a ROS Package`
1. Go to workspace ros
	- `$ cd ~/catkin_ws/src`
2. Create directory project
	- `$ mkdir ROS-RaspberryPi-Basic`
	- `$ cd ROS-RaspberryPi-Basic`
3. Create a catkin package
	- `$ catkin_create_pkg aa_contoh_package std_msgs rospy roscpp`
4. Build a catkin workspace
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
5. Sourcing the Setup file
	- `$ . ~/catkin_ws/devel/setup.bash`

## `ROS Node`
> Test ros node
1. Go to workspace ros
	- `$ cd ~/catkin_ws/src`
2. Run roscore
	- `$ roscore`
3. Check node with rosnode list
	- `$ rosnode list`<br/>
	will be show `/rosout`,it is a node running
4. Check info inside of a `/rosout` node
	- `$ rosnode info /rosout`

> Try another example, turtlesim_node
note: if turtlesim node not yet already installed on your os, please following instruction below
- `$ sudo apt-get install ros-kinetic-turtlesim`
- `$ sudo rosdep init`
- `$ rosdep update`
- `$ source /opt/ros/kinetic/setup.bash`

1. Go to workspace ros
	- `$ cd ~/catkin_ws/src`
2. Run roscore
	- `$ roscore`
3. Run the node using rosrun
	- `$ rosrun turtlesim turtlesim_node`
4. Check nodes with rosnode list
	- `$ rosnode list`
5. Check info inside of a `/rosout` node
	- `$ rosnode info /rosout` atau
	- `$ rosnode info /turtlesim`

## `ROS Topic`
> Try turtlesim_node to explore ros topic function
1. Go to workspace ros
	- `$ cd ~/catkin_ws/src`
2. Run roscore
	- `$ roscore`
3. Run the node using rosrun
	- `$ rosrun turtlesim turtlesim_node`
4. Check nodes with rosnode list
	- `$ rosnode list`
5. Run turtle_teleop_key topic
	- `$ rosrun turtlesim turtle_teleop_key`

> Try another example topic, rqt_graph
note: if rqt_graph not yet already installed on your os, please following instruction below
- `$ sudo apt-get install ros-kinetic-rqt-common-plugins`
1. Go to workspace ros
	- `$ cd ~/catkin_ws/src`
2. Run roscore
	- `$ roscore`
3. Run the node using rosrun
	- `$ rosrun turtlesim turtlesim_node`
4. Run turtle_teleop_key topic
	- `$ rosrun turtlesim turtle_teleop_key`
5. Run the rqt_graph using rosrun
	- `$ rosrun rqt_graph rqt_graph`

#### ROS Topic sub-commands
Type `$ rostopic -h`<br/>
| rostopic | Description |
| -------- | ----------- |
| rostopic bw | display bandwidth used by topic |
| rostopic delay | display delay of topic from timestamp in header |
| rostopic echo | print messages to screen |
| rostopic find | find topics by type |
| rostopic hz | display publishing rate of topic |    
| rostopic info | print information about active topic |
| rostopic list | list active topics |
| rostopic pub | publish data to topic |
| rostopic type | print topic or field type |


How to test the topics
1. Open a new terminal
2. Try the rostopic echo. Type
	- `$ rostopic echo /turtle1/cmd_vel`
	- Move the turtle1 using turtle_teleop_key
	- Have a look on the terminal. It will show the information about cmd_vel node
3. Try the rostopic list -v
	- `$ rostopic list -v`
	- It will show the active topics

#### ROS Message
1. Make sure the command below has been executed
	- `$ roscore`
	- `$ rosrun turtlesim turtlesim_node`
2. Open a new terminal and exucute
	- `$ rostopic type /turtle1/cmd_vel`
	- Shoud get geometry_msgs/Twist
3. Show the details of mesage using rosmsg
	- `$ rosmsg show geometry_msgs/Twist`

#### ROS Topic pub
rostopic pub publishes data on to a topic current advertised
1. Make sure the command below has been executed
	- `$ roscore`
	- `$ rosrun turtlesim turtlesim_node`
2. Try to move turtle1 use rostopic pub
	- `$ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'`
	- for more info please visit [wiki.ros.org/ROS/Tutorials/UnderstandingTopics](wiki.ros.org/ROS/Tutorials/UnderstandingTopics)

#### ROS Topic hz
rostopic hz reports the rate at which data is published
1. Make sure the command below has been executed
	- `$ roscore`
	- `$ rosrun turtlesim turtlesim_node`
2. Execute the rostopic hz
	- `$ rostopic hz /turtle1/pose`

## `rqt_plot`
1. Install rqt_plot. If already installed please skip this step
	- Note: make sure `$ pip list --upgrade pip` and `$ python -m pip install -U matplotlib`
	- `$ sudo apt-get install ros-kinetic-rqt`
	- `$ sudo apt-get install ros-kinetic-rqt-common-plugins`
2. Make sure the command below has been executed
	- `$ roscore`
	- `$ rosrun turtlesim turtlesim_node`
	- `$ rosrun turtlesim turtle_teleop_key`
3. Execute the rqt_plot
	- `$ rosrun rqt_plot rqt_plot`
4. In the rqt_plot window, fill Topic with
	- `/turtle/pose/x` and enter
	- `/turtle/pose/y` and enter
5. Go to terminal turtle_teleop_key and press arrow button to move the turtle
6. See what happened to the rqt_plot window
7. Amazing kan
8. Test rqt_console and rqt_logger_level for debuging
	- Execute `$ rosrun rqt_console rqt_console`
	- Execute `$ rosrun rqt_logger_level rqt_logger_level`
	- Move the turlesim with turtle_teleop_key until reach the end of window
	- See on the rqt_console and rqt_logger_level windows will show information


## `ROS Service`
1. Make sure the command below has been executed
	- `$ roscore`
	- `$ rosrun turtlesim turtlesim_node`
	- `$ rosrun turtlesim turtle_teleop_key`
2. How to check the active rosservice
	- `$ rosservice list`
3. How to check the rosservice type
	- `$ rosservice type /clear`
	- `$ rosservice type /kill`
	- `$ rosservice type /reset`
	- `$ rosservice type /spawn`
	- etc
3. How to check the rosservice arguments
	- `$ rosservice type /clear | rossrv show`
	- `$ rosservice type /kill  | rossrv show`
	- `$ rosservice type /reset | rossrv show`
	- `$ rosservice type /spawn | rossrv show`
	- etc
5. How to call the rosservice
	- `$ rosservice call /clear`
	- `$ rosservice call /kill "name: 'turtle1'"`
	- `$ rosservice call /reset `
	- `$ rosservice call /spawn "x: 1.0
		 y: 2.0
		 theta: 0.0
		 name: 'kurakura'"`
	- etc

## `ROS Parameter`
1. Make sure the command below has been executed
	- `$ roscore`
	- `$ rosrun turtlesim turtlesim_node`
2. How to find out which parameters are active is to execute the program below
	- `$ rosparam list`
	- Will show all active parameters
3. How to run `rosparams set`
	- `$ rosparam set /background_b 150`
	- `$ rosservice call /clear`
4. How to run `rosparams get`
	- `$ rosparam get /background_b`

## `ROS Launch`
roslaunch is package which use to run file together like node, etc
1. Creating a new ros package
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic`
	- `$ catkin_create_pkg ab_roslaunch std_msgs rospy`
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
	- `$ . ~/catkin_ws/devel/setup.bash`
2. Create README.md file for notes
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ab_roslaunch`
	- `$ touch README.md`
3. For further tutorials about ROS Launch please visit [https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ab_roslaunch](https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ab_roslaunch)

## `msg`
msg are simple text file that describe the fields of a ROS message
1. Creating a new ros package
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic`
	- `$ catkin_create_pkg ac_contoh_msg std_msgs rospy`
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
	- `$ . ~/catkin_ws/devel/setup.bash`
2. Create README.md file for notes
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ac_contoh_msg`
	- `$ touch README.md`
3. For further this tutorials about ROS message please visit [https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ac_contoh_msg](https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ac_contoh_msg)

## `srv`
srv have a request and a response
1. Creating a new ros package
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic`
	- `$ catkin_create_pkg ad_contoh_srv std_msgs rospy`
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
	- `$ . ~/catkin_ws/devel/setup.bash`
2. Create README.md file for notes
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ad_contoh_srv`
	- `$ touch README.md`
3. For further this tutorials about ROS message please visit [https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ad_contoh_srv](https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ad_contoh_srv)

## `Publisher and Subscriber - Python`
1. Creating a new ros package
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic`
	- `$ catkin_create_pkg ae_publisher_and_subscriber_python std_msgs rospy`
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
	- `$ . ~/catkin_ws/devel/setup.bash`
2. Create README.md file for notes
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ae_publisher_and_subscriber_python`
	- `$ touch README.md`
3. For further this tutorials about ROS message please visit [https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ae_publisher_and_subscriber_python](https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ae_publisher_and_subscriber_python)

## `Service and Client`
1. Creating a new ros package
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic`
	- `$ catkin_create_pkg af_service_and_client std_msgs rospy`
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
	- `$ . ~/catkin_ws/devel/setup.bash`
2. Create README.md file for notes
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/af_service_and_client`
	- `$ touch README.md`
3. For further this tutorials about ROS message please visit [https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/af_service_and_client](https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/af_service_and_client)

## `ROSBAG`
1. Create a new directory
	- Open a new terminal
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic`
	- `$ mkdir ag_rosbag`
	- `$ cd ag_rosbag`
	- `$ touch README.md`
2. For further this tutorials about ROS message please visit [https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ag_rosbag](https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ag_rosbag)

## `Action`
1. Creating a new ros package
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic`
	- `$ catkin_create_pkg ah_action std_msgs rospy`
	- `$ cd ~/catkin_ws`
	- `$ catkin_make`
	- `$ . ~/catkin_ws/devel/setup.bash`
2. Create README.md file for notes
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ah_action`
	- `$ touch README.md`
3. For further this tutorials about ROS message please visit [https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ah_action](https://github.com/wildenali/ROS-RaspberryPi-Basic/tree/master/ah_action)
