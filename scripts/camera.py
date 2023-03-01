#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
from adafruit_servokit import ServoKit
import time

def callback(data):
    print("Test")
    global kit
    global servo_cero
    try:
        rospy.Rate(rospy.get_param('~hz',100))
        kit.servo[servo_cero].angle = int(data.data)        
        rospy.loginfo(rospy.get_caller_id() +"Value: "+str(data.data))
        
    except Exception as e:
        print(data.data)
        print(e)

def listener():

    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('/arm_teleop/cam',Int32,callback)
    rospy.spin()

if __name__ == '__main__':
    print("Enter main")
    kit = ServoKit(channels=16)
    servo_cero = 4
    kit.servo[servo_cero].set_pulse_width_range(1000,2000)
    kit.servo[servo_cero].actuation_range=180
    listener()
