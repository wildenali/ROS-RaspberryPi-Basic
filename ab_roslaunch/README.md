# ROS Launch
In this tutorial, we will create a launch file to launch 2 pieces of turtlesim
1. Create a directory called `launch`
	- Open a terminal
	- `$ cd ~/catkin/src/ROS-RaspberryPi-Basic/ab_roslaunch`
	- `$ mkdir launch`
	- `$ cd launch`
2. Create a launch file called `ab_tutlesim.launch`
	- `$ touch ab_turtlesim.launch`
3. Create a code in the ab_turtlesim.launch file like below
	```sh
	<launch>
	
		<group ns="turtlesim1">
			<node pkg="turtlesim" name="kurakura_1" type="turtlesim_node"/>
		</group>

		<group ns="turtlesim2">
			<node pkg="turtlesim" name="kurakura_2" type="turtlesim_node"/>
		</group>
		
		<node pkg="turtlesim" name="ab_kurakura_launch" type="mimic">
			<remap from="input" to="turtlesim1/turtle1"/>
			<remap from="input" to="turtlesim2/turtle2"/>
		</node>
	
	</launch>

	```
4. Build package
	- Open a new terminal
	- `$ cd ~/catkin_ws`
	- `$ roslaunch ab_roslaunch ab_turtlesim.launch`
5. Test rostopic pub
	- Open a new terminal
	- `$ rostopic pub -1 /turtlesim1/turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'`
