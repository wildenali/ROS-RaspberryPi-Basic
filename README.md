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

