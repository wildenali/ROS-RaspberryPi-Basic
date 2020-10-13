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
