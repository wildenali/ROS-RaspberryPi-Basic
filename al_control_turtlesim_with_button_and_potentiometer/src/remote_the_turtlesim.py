#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

def callback_Button(data):
	velocity_msg = Twist()
	button_values = data.data
	if button_values == 0:
		velocity_msgs.linear.x = 0.3
		print("Moving forward---->")
	else:
		velocity_msgs.linear.x = 0
		print("STOP")
	velocity_pub.publish(velocity_msg)
	
def control_turtlesim():
	rospy.init_node('turtlesim_button_potentiometer_control', anonymous = True)
	rospy.Subscriber('/values', Int32, callback_Button)
	rospy.spin()

if __name__ == '__main__':
	print("Getting data from Button")
	velocity_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
	control_turtlesim()
