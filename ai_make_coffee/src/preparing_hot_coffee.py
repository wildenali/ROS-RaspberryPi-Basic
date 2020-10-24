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
