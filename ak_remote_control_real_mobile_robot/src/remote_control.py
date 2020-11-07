#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import socket

message = "0"

class driver:
	def __init__(self):
		# init ros
		rospy.init_node('car_driver', anonymous=True)
		rospy.Subscriber('/cmd_vel', Twist, self.get_cmd_vel)
		self.get_arduino_message()
	
	# get cmd_vel message, and get linear velocity and angular velocity
	def get_cmd_vel(self, data):
		linear = data.linear.x
		rotation = data.angular.z
		self.send_cmd_to_arduino(int(linear), int(rotation))
		
	# translate x, and angular velocity to PWM signal of each wheels and send to arduino
	def send_cmd_to_arduino(self, linear, rotation):
		global message
		message = "{},{},*".format(linear,rotation)
		print("Linear", linear, "----", "Angular", rotation)
		
		# send by serial
		sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
	
	# receive serial text from arduino and publish it to '/arduino' message
	def get_arduino_message(self):
		global message
		print("MESSAGE", message)
		pub = rospy.Publisher('arduino', String, queue_size=10)
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			pub.publish(message)
			r.sleep()

if __name__ == '__main__':
	UDP_IP = "192.168.0.22"		# esp866 ip and port
	UDP_PORT = 8888
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	try:
		driver()
	except rospy.ROSInterruptException:
		pass

