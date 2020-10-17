#!/usr/bin/env python

import sys
import rospy

from af_service_and_client.srv import af_penjumlahan
from af_service_and_client.srv import af_penjumlahanRequest
from af_service_and_client.srv import af_penjumlahanResponse

def penjumlahanClient(x,y):
	rospy.wait_for_service('penjumlahan')
	try:
		penjumlahan = rospy.ServiceProxy('penjumlahan', af_penjumlahan)
		respon1 = penjumlahan(x,y)
		return respon1.sum
	except rospy.ServiceException, e:
		print("Service GAGAL di panggil: %s" %e)

def usage():
	return "%s [x y]" %sys.argv[0]

if __name__ == '__main__':
	if len(sys.argv) == 3:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
	else:
		print(usage())
		sys.exit(1)
	
	print("Rekues in %s + %s" %(x,y))
	print("%s + %s = %s" %(x,y, penjumlahanClient(x,y)))
