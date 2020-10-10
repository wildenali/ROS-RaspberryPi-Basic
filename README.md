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
<br/>
How to test the topics
1. Open a new terminal
2. Try the rostopic echo. Type
	- `$ rostopic echo /turtle1/cmd_vel`
	- Move the turtle1 using turtle_teleop_key
	- Have a look on the terminal. It will show the information about cmd_vel node
3. Try the rostopic list -v
	- `$ rostopic list -v`
	- It will show the active topics
