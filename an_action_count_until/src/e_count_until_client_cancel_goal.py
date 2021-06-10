#!/usr/bin/env python

import rospy
import actionlib

from an_action_count_until.msg import CountUntilAsyncAction, CountUntilAsyncGoal

class CountUntilClient:
	def __init__(self):
		self._ac = actionlib.SimpleActionClient('/count_until_cancel_goal', CountUntilAsyncAction)
		self._ac.wait_for_server()
		rospy.loginfo("Action Server Cancel Goal is up, we can send new goals!")
	
	def send_goal_and_get_result(self):
		goal = CountUntilAsyncGoal(max_number=10, wait_duration=0.5)	# coba ganti2 nilainya, misal max_number nya dari 5 15 dan 20
		self._ac.send_goal(goal, done_cb=self.done_callback, feedback_cb=self.feedback_callback)	# create feedback
		rospy.loginfo("Goal has been sent")
		
		rospy.sleep(2)
		self._ac.cancel_goal()
	
	def done_callback(self, status, result):
		rospy.loginfo("Status is : " + str(status))
		rospy.loginfo("Result is : " + str(result))
		
	def feedback_callback(self, feedback):		# callback feeedback
		rospy.loginfo(feedback)
		rospy.loginfo("persentasinya: " + str(feedback.percentage))
	
if __name__ == '__main__':
	rospy.init_node('count_until_client_cancel_goal')
	
	client = CountUntilClient()
	
	client.send_goal_and_get_result()
	
	rospy.spin()
