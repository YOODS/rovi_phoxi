#!/usr/bin/python

import numpy as np
import cv2
import glob
import sys

import roslib
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

Config={
  "img":"../.PhotoneoPhoXiControl/Output/scan*.png"
}

ImgFile=''
ImgDat=None

def cb_fchk(msg):
  global ImgFile,ImgDat
  dl=glob.glob(Config["img"])
  if len(dl)>0:
    dl.sort(reverse=True)
    if ImgFile!=dl[0]:
      im=cv2.imread(dl[0])
      print "imread",dl[0]
      im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY);
      ImgDat=bridge.cv2_to_imgmsg(im,'mono8')
      ImgFile=dl[0]
    if ImgDat is not None: impub.publish(ImgDat)
  rospy.Timer(rospy.Duration(1),cb_fchk,oneshot=True)
  return

def parse_argv(argv):
  args={}
  for arg in argv:
    tokens = arg.split(":=")
    if len(tokens) == 2:
      key = tokens[0]
      args[key]=tokens[1]
  return args

########################################################
rospy.init_node("fdriver",anonymous=True)
Config.update(parse_argv(sys.argv))
try:
  Config.update(rospy.get_param("~config"))
except Exception as e:
  print "get_param exception:",e.args
print "Config",Config

bridge=CvBridge()
impub=rospy.Publisher('~image_raw',Image,queue_size=1)

rospy.Timer(rospy.Duration(1),cb_fchk,oneshot=True) #to check change of file
try:
  rospy.spin()
except KeyboardInterrupt:
  print "Shutting down"
