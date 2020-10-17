#!/usr/bin/env python

from af_service_and_client.srv import af_penjumlahan
from af_service_and_client.srv import af_penjumlahanRequest
from af_service_and_client.srv import af_penjumlahanResponse

import rospy

def handlePenjumlahan(rekuest):
	#print(rekuest)
	print("Hasilnya adalah: %s + %s = %s" %(rekuest.a, rekuest.b, (rekuest.a + rekuest.b)))
	return af_penjumlahanResponse(rekuest.a + rekuest.b)

def penjumlahanServer():
	rospy.init_node('penjumlahan_server')
	s = rospy.Service('penjumlahan', af_penjumlahan, handlePenjumlahan)
	print("Server udah siap nih, Ayo jumlahin")
	rospy.spin()

if __name__ == '__main__':
	penjumlahanServer()
