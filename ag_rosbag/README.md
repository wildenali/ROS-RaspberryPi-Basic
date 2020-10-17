# ROSBAG
Rosbag adalah set of tools untuk merekam dan memutar ulang ROS topic.
rosbag ini dapat merekam data dari sistem ROS yg sedang berjalan dan dapat di
putar ulang sirekaman tersebut.

References:
- [https://wiki.ros.org/ROS/rosbag/Tutorials/](https://wiki.ros.org/ROS/rosbag/Tutorials/) 

## `a_recording_and_playing_back_data`
Kita akan recording and playing back pergerakan turtlesim
1. Creata a new directory to save bag file called `a_recording_and_playing_back_data`
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ag_rosbag`
	- `$ mkdir a_recording_and_playing_back_data`
	- `$ cd a_recording_and_playing_back_data`
2. Run turlesim node and turtle teleop
	- Run roscore `$ roscore`
	- Open a new terminal and run turtlesim `$ rosrun turtlesim turtlesim_node`
	- Open a new terminal and run turtle_teleop_key `$ rosrun turtlesim turtle_teleop_key`
	- Check the full list of topics, Open a new terminal and type `$ rostopic list -v`
3. Recording data (creating a bag file)
	- Open a new terminal and type `$ rosbag record -a`
	- Move back to `turtle_teleop_key` terminal and move the turtle around for 10 or so seconds
	- To stop recording please Ctrl+C on the `rosbag record -a` terminal
4. Check rosbag file
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ag_rosbag/a_recording_and_playing_back_data`
	- `$ rosbag info 2020-10-17-10-50-17.bag`
4. Play back rosbag file
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ag_rosbag/a_recording_and_playing_back_data`
	- Reset the turtlesim `$ rosservice call /reset`
	- `$ rosbag play 2020-10-17-10-50-17.bag`
