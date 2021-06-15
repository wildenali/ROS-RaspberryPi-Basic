#!/usr/bin/env python

import rospy
import actionlib
from ao_action_move_robot.msg import MoveRobotAction
from ao_action_move_robot.msg import MoveRobotGoal

class MoveRobotClient:
	def __init__(self):
		self._ac = actionlib.SimpleActionClient('/move_robot', MoveRobotAction)
		self._ac.wait_for_server()
		rospy.loginfo("Server is up, let's send a goal")
	
	def send_goal(self):
		goal = MoveRobotGoal()
		goal.position = 77
		goal.velocity = 5
		self._ac.send_goal(goal, done_cb=self.done_callback, feedback_cb=self.feedback_callback)
	
	def done_callback(self, status, result):
		rospy.loginfo("Status: " + str(status))
		rospy.loginfo("Result: " + str(result))
		
	def feedback_callback(self, feedback):
		rospy.loginfo(feedback)

if __name__ == '__main__':
	rospy.init_node('move_robot_client')
	
	client = MoveRobotClient()
	client.send_goal()
	
	rospy.spin()
