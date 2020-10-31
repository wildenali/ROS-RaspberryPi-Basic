#!/usr/bin/env python

from aj_service_move_turtlesim.srv import *
import rospy

def concatinate_Name(req):
	print(req)
	return newResponse(req.name1 + req.name2)

def security_Server():
	rospy.init_node('security')
	s = rospy.Service('name_confirmation', new, concatinate_Name)
	print("Udah siap nih server, Ayo cuus")
	rospy.spin()

if __name__ == '__main__':
	security_Server()
