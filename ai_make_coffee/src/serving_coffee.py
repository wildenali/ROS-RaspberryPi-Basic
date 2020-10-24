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
