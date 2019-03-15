#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix

def trackGPSposition(positionCallback):
    latitude = positionCallback.latitude
    longitude = positionCallback.longitude
    print ("longitude: %.7f" %longitude)
    print ("latitude: %.7f" %latitude)

if __name__ == '__main__':
    
    rospy.init_node('BasicSubscriber', anonymous=True)
    
    while True:
            
        rospy.Subscriber("/mavros/global_position/raw/fix", NavSatFix, positionCallback)
        trackGPSposition(positionCallback)
        
    
