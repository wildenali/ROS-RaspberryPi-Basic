#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(pesan):
	# get called id(): Get fully resolve name of local node
	print(pesan)
	rospy.loginfo(rospy.get_caller_id() + "Berhitung woy %s", pesan.data)

def listener():
	rospy.init_node('py_subscriber', anonymous=True)
	rospy.Subscriber('py_kirim', String, callback)
	
	rospy.spin()

if __name__ == '__main__':
	listener()
