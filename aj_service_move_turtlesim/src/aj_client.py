#!/usr/bin/env python

import sys
import rospy
from geometry_msgs.msg import Twist
from aj_service_move_turtlesim.srv import *

def concate_name_client(x, y):
	rospy.wait_for_service('name_confirmation')
	concat_name = rospy.ServiceProxy('name_confirmation', new)
	resp1 = concat_name(x, y)
	return resp1

def useage():
	return "%s [x y]" %sys.argv[0]

def security_Verifying():
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist)
	rospy.sleep(1)
	r = rospy.Rate(5.0)
	while not rospy.is_shutdown():
		twist = Twist()
		twist.linear.x = 0.3
		for i in range(10):
			pub.publish(twist)
			r.sleep()
		
		twist = Twist()
		twist.angular.z = 1.57/2
		for i in range(10):
			pub.publish(twist)
			r.sleep()

if __name__ == '__main__':
	rospy.init_node('move_after_security')
	if len(sys.argv) == 3:
		x = sys.argv[1]
		y = sys.argv[2]
	else:
		print(useage())
		sys.exit(1)
	
	result = concate_name_client(x, y)
	if (result.fullname) == "WildenAli":
		security_Verifying()
	else :
		print("Salah Orang")
