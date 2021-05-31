#!/usr/bin/env python

import rospy
import actionlib

from an_action_count_until.msg import CountUntilAsyncAction, CountUntilAsyncGoal

class CountUntilClient:
	def __init__(self):
		self._ac = actionlib.SimpleActionClient('/count_until_async', CountUntilAsyncAction)
		self._ac.wait_for_server()
		rospy.loginfo("Action Server Async is up, we can send new goals!")
	
	def send_goal_and_get_result(self):
		goal = CountUntilAsyncGoal(max_number=10, wait_duration=0.5)	# coba ganti2 nilainya, dan amati apa yg terjadi
		self._ac.send_goal(goal, done_cb=self.done_callback)
		rospy.loginfo("Goal has been sent")
		# self._ac.wait_for_result()
		# rospy.loginfo(self._ac.get_result())
	
	def done_callback(self, status, result):
		rospy.loginfo("Status is : " + str(status))
		rospy.loginfo("Result is : " + str(result))
		
if __name__ == '__main__':
	rospy.init_node('count_until_client_async')
	
	client = CountUntilClient()
	
	client.send_goal_and_get_result()
	
	rospy.spin()
