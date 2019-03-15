#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from mavros_msgs.srv import *

rospy.init_node('BasicCmdServices', anonymous=True)
#http://wiki.ros.org/mavros/CustomModes for search your custom modes

def setMode(mode):
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode=mode)
    except (rospy.ServiceException, e):
        print ("service set_mode call failed: %s. GUIDED Mode could not be set. Check that GPS is enabled"%e)

def setLandMode():
    rospy.wait_for_service('/mavros/cmd/land')
    try:
        landService = rospy.ServiceProxy('/mavros/cmd/land', mavros_msgs.srv.CommandTOL)
        isLanding = landService(altitude = 0, latitude = 0, longitude = 0, min_pitch = 0, yaw = 0)
    except (rospy.ServiceException, e):
        print ("service land call failed: %s. The vehicle cannot land "%e)
          
def setArm():
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        armService = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
        armService(True)
    except (rospy.ServiceException, e):
        print ("Service arm call failed: %s"%e)
        
def setDisarm():
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        armService = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
        armService(False)
    except (rospy.ServiceException, e):
        print ("Service arm call failed: %s"%e)


def setTakeoffMode(targetAltitude):
    rospy.wait_for_service('/mavros/cmd/takeoff')
    try:
        takeoffService = rospy.ServiceProxy('/mavros/cmd/takeoff', mavros_msgs.srv.CommandTOL) 
        takeoffService(altitude = targetAltitude, latitude = 0, longitude = 0, min_pitch = 0, yaw = 0)
    except (rospy.ServiceException, e):
        print ("Service takeoff call failed: %s"%e)

#do code here

