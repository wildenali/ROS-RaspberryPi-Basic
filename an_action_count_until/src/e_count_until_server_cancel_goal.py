#!/usr/bin/env python

import rospy
import actionlib

from an_action_count_until.msg import CountUntilAsyncAction
from an_action_count_until.msg import CountUntilAsyncGoal
from an_action_count_until.msg import CountUntilAsyncResult
from an_action_count_until.msg import CountUntilAsyncFeedback

class CountUntilServer:
  def __init__(self):
    self._as = actionlib.SimpleActionServer('/count_until_cancel_goal', CountUntilAsyncAction, execute_cb=self.on_goal, auto_start=False)
    self._as.start()

    self._counter = 0
    rospy.loginfo("Simple Action Cancel Goal Server has been started")
  
  def on_goal(self, goal):
    rospy.loginfo("A goal has been received!")
    rospy.loginfo(goal)

    max_number = goal.max_number
    wait_duration = goal.wait_duration

    self._counter = 0
    rate = rospy.Rate(1.0/wait_duration)
    
    success = False
    preempted = False
    
    while not rospy.is_shutdown():
      self._counter += 1
      if self._as.is_preempt_requested():	# cara cancel goal
        preempted = True
        break
      if self._counter > 9:		# coba di ...action.py file nya ganti jadi angka lebih dari 20 misalnya
        succces = False
        break
      if self._counter >= max_number:
        success = True
        break
      rospy.loginfo(self._counter)
      feedback = CountUntilAsyncFeedback()								# create feedback
      feedback.percentage = float(self._counter) / float(max_number)	# percentage feedback
      self._as.publish_feedback(feedback)
      rate.sleep()

    result = CountUntilAsyncResult()
    result.count = self._counter
    rospy.loginfo("Send goal result to client")
    
    if preempted:
      rospy.loginfo("preempted")
      self._as.set_preempted(result)
    elif success:
      rospy.loginfo("Sukses")
      self._as.set_succeeded(result)
    else:
      rospy.loginfo("Gagal")
      self._as.set_aborted(result)

if __name__ == '__main__':
  rospy.init_node('count_until_server_cancel_goal')
  
  server = CountUntilServer()

  rospy.spin()
