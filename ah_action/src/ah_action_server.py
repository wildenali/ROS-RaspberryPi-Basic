#!/usr/bin/env python

import rospy
import time
import actionlib	# import ini untuk menggunakan SimplaActionServer class
from ah_action.msg import TimerAction, TimerGoal, TimerResult

def doTimer(goal):	# fungsi program timer, fungsi ini dibuat untuk menghitung berapa lama waktu ketika server menerima pesan goal yg dikirim oleh client
	start_time = time.time()
	time.sleep(goal.time_to_wait.to_sec())
	result = TimerResult()
	result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)		# ini menghitung berapa lamanya
	result.updates_sent = 0
	server.set_succeeded(result)

rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, doTimer, False)
server.start()
rospy.spin()
