References:
- ROS Ultimate Guide to Beginners Guide Hands ON! by Muhammad Luqman on udemy.com course

# Publisher - coffee_ingredients.py
1. Creata a publisher file called `coffee_ingredients.py`
	- `$ cd src`
	- `$ touch coffee_ingredients.py`
	- `$ chmod +x coffee_ingredients.py`	change the permissions
2. Edit the `coffee_ingredients.py` file like below
	```sh
	#!/usr/bin/env python

	import rospy
	from std_msgs.msg import String

	def publishing():
		pub = rospy.Publisher('coffee_ingredients', String, queue_size = 10)
		rospy.init_node('kopi_ingredients', anonymous = True)
		rate = rospy.Rate(10)	# 10 hz
		
		while not rospy.is_shutdown():
			data = "sugar,milk,coffee"
			rospy.loginfo(data)
			pub.publish(data)
			rate.sleep()

	if __name__ == '__main__':
		try:
			publishing()
		except rospy.ROSInterruptException:
			pass
	```
3. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/coffee_ingredients.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
4. Build the node
	- Open a terminal
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`
5. Run the node
	- `$ cd ~/catkin_ws/`
	- `$ roscore`
	- Open a new terminal and type `$ rosrun ai_make_coffee coffee_ingredients.py`
	- Close the all terminal to stop it

# Subscriber and Publisher - preparing_hot_coffee.py	
1. Creata a subscriber and publisher file called `preparing_hot_coffee.py`
	- Open a new terminal
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ai_make_coffee`
	- `$ cd src`
	- `$ touch preparing_hot_coffee.py`
	- `$ chmod +x preparing_hot_coffee.py`	change the permissions, type `$ la -la` to check permissions status
2. Edit the `preparing_hot_coffee.py` file like below
	```sh
	#!/usr/bin/env python

	import rospy
	from std_msgs.msg import String

	def callback(inipesan):
		print(inipesan.data)
		inipesan = inipesan.data + ' cangkir'
		pub.publish(inipesan)
		
	def listener():
		rospy.init_node('preparing_hot_coffee', anonymous=True)
		rospy.Subscriber('coffee_ingredients', String, callback)
		
		rospy.spin()

	if __name__ == '__main__':
		pub = rospy.Publisher('your_kopi', String, queue_size = 10)
		listener()
	```
3. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/coffee_ingredients.py
			src/preparing_hot_coffee.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
4. Build the node
	- Open a terminal
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`
5. Run the node
	- `$ roscore`
	- Open a new terminal and type `$ rosrun ai_make_coffee coffee_ingredients.py`
	- Open a new terminal and type `$ rosrun ai_make_coffee preparing_hot_coffee.py`

# Subscriber - serving_coffee.py	
1. Creata a subscriber file called `serving_coffee.py`
	- Open a new terminal
	- `$ cd ~/catkin_ws/src/ROS-RaspberryPi-Basic/ai_make_coffee`
	- `$ cd src`
	- `$ touch serving_coffee.py`
	- `$ chmod +x serving_coffee.py`	change the permissions, type `$ la -la` to check permissions status
2. Edit the `serving_coffee.py` file like below
	```sh
	#!/usr/bin/env python

	import rospy
	from std_msgs.msg import String

	def callback(pesan):
		print(pesan.data)
		
	def listener():
		rospy.init_node('serving_coffee', anonymous=True)
		rospy.Subscriber('your_kopi', String, callback)
		
		rospy.spin()

	if __name__ == '__main__':
		listener()
	```
3. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/coffee_ingredients.py
			src/preparing_hot_coffee.py
			src/serving_coffee.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
4. Build the node
	- Open a terminal
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`
5. Run the node
	- `$ roscore`
	- Open a new terminal and type `$ rosrun ai_make_coffee coffee_ingredients.py`
	- Open a new terminal and type `$ rosrun ai_make_coffee preparing_hot_coffee.py`
	- Open a new terminal and type `$ rosrun ai_make_coffee serving_coffee.py`
