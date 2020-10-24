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
