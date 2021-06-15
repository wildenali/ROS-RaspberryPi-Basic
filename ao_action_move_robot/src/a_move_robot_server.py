#!/usr/bin/env python

import rospy
import actionlib
from ao_action_move_robot.msg import MoveRobotAction
from ao_action_move_robot.msg import MoveRobotFeedback
from ao_action_move_robot.msg import MoveRobotResult

class MoveRobotServer:
	def __init__(self):
		# _as adalah action server
		self._as = actionlib.SimpleActionServer('/move_robot', MoveRobotAction, execute_cb=self.on_goal, auto_start=False)
		self._as.start()
		
		self._current_position = 50
		rospy.loginfo("Server has been started")
	
	def send_feedback(self):
		feedback = MoveRobotFeedback()
		feedback.current_position = self._current_position
		self._as.publish_feedback(feedback)
	
	def on_goal(self, goal):
		rospy.loginfo("A Goal has been received")
		rospy.loginfo(goal)
		
		goal_position = goal.position
		velocity = goal.velocity
		
		success = False
		preempted = False
		invalid_parameters = False
		message = ""
		rate = rospy.Rate(1.0)
		
		if goal_position < 0 or goal_position > 100:
			message = "Invalid goal position, must be [0-100]"
			invalid_parameters = True
		
		if goal_position == self._current_position:
			success = True
			message = "Current position is already correct"
		
		while not rospy.is_shutdown() and not success and not invalid_parameters:
			if self._as.is_preempt_requested():
				if goal_position == self._currentposition:
					message = "Preempted but already at goal position"
					success = True
				else:
					message = "Preempted and stopped execution"
					preempted = True
				break
			
			diff = goal_position - self._current_position
			
			if diff == 0:
				message = "Success"
				success = True
				break
			elif diff < 0:
				if abs(diff) >= velocity:
					self._current_position -= velocity
				else:
					self._current_position -= abs(diff)
			elif diff > 0:
				if diff >= velocity:
					self._current_position += velocity
				else:
					self._current_position += diff
			
			self.send_feedback()
			rate.sleep()	# biar while nya ga terlalu fast, klo mau fast, ga usah pake rate.sleep()
		
		result = MoveRobotResult()
		result.position = self._current_position
		result.message = message
		
		if preempted:
			rospy.loginfo("Preempted")
			self._as.set_preempted(result)
		elif success:
			rospy.loginfo("Success")
			self._as.set_succeeded(result)
		else:
			rospy.loginfo("Aborted")
			self._as.set_aborted(result)

if __name__ == '__main__':
	rospy.init_node('move_robot_server')
	
	server = MoveRobotServer()
	
	rospy.spin()
