# Publisher and Subscriber - Python
In this tutorial, we will learn how to publish data and subscribe data using python

References:
- [https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29](https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29) 

1. Creata a publisher file called `pub.py`
	- `$ cd src`
	- `$ touch pub.py`
	- `$ chmod +x pub.py`	change the permissions
2. Edit the `pub.py` file like below
	```sh
	#!/usr/bin/env python

	# license removed for brevity
	import rospy
	from std_msgs.msg import String

	def pengirim():
		# membuat publisher baru, dengan spesifik nama 'py_kirim', dan queue_size = 10
		pub = rospy.Publisher('py_kirim', String, queue = 10)
		
		# inisialisasi node dulu dengan nama 'py_publisher'
		rospy.init_node('py_publisher', anonymous = True)
		
		# set the loop rate
		rate = rospy.Rate(1)	# 10 hz
		
		i = 0
		while not rospy.is_shutdown():
			hellow = "heylow ini ke %s" %i
			rospy.loginfo(hellow)
			pub.publish(hellow)
			rate.sleep()
			i += 1

	if __name__ == '__main__':
		try:
			pengirim()
		except rospy.ROSInterruptException:
			pass
	
	```
3. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/pub.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
4. Build the node
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`
5. Run the node
	- `$ cd ~/catkin_ws/`
	- `$ roscore`
	- Open a new tab and type `$ rosrun ae_publisher_and_subscriber_python pub.py`
	- Close the all terminal to stop it
	
6. Creata a subscriber file called `sub.py`
	- Open a new terminal
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ae_publisher_and_subscriber_python`
	- `$ cd src`
	- `$ touch sub.py`
	- `$ chmod +x sub.py`	change the permissions, type `$ la -la` to check permissions status
7. Edit the `sub.py` file like below
	```sh
	#!/usr/bin/env python

	import rospy
	from std_msgs.msg import String

	def callback(pesan):
		# get called id(): Get fully resolve name of local node
		rospy.loginfo(rospy.get_caller_id() + "Berhitung woy %s", pesan.data)

	def listener():
		rospy.init_node('py_subscriber', anonymous=True)
		rospy.Subscriber('py_kirim', String, callback)
		
		rospy.spin()

	if __name__ == '__main__':
		listener()
	```
8. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/pub.py
			src/sub.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
9. Build the node
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`
10. Run the node
	- `$ roscore`
	- Open a new tab and type `$ rosrun ae_publisher_and_subscriber_python pub.py`
	- Open a new tab and type `$ rosrun ae_publisher_and_subscriber_python sub.py`
