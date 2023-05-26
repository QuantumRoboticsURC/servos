#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
from adafruit_servokit import ServoKit
import time
def limits(data, liminf,limsup):
    if data<liminf:
        data=liminf
    elif data>limsup:
        data=limsup
    return data



def callback(data):
    print("Test")
    global kit
    global servo_camArm
    try:
        rospy.Rate(rospy.get_param('~hz',100))
        ndata=limits(data.data,0,180)
        kit.servo[servo_camArm].angle = int(ndata)        
        rospy.loginfo(rospy.get_caller_id() +"Value: "+str(data.data))
        
    except Exception as e:
        print(data.data)
        print(e)

def callback2(data):
    print("Test")
    global kit
    global servo_camAntena
    try:
        rospy.Rate(rospy.get_param('~hz',100))
        ndata=limits(data.data,0,180)
        kit.servo[servo_camAntena].angle = int(ndata)        
        rospy.loginfo(rospy.get_caller_id() +"Value: "+str(data.data))
        
    except Exception as e:
        print(data.data)
        print(e)

def callback3(data):
    print("Test")
    global kit
    global servo_rotacion
    try:
        rospy.Rate(rospy.get_param('~hz',100))
        ndata=limits(data.data,191,281)
        kit.servo[servo_rotacion].angle = int(ndata)        
        rospy.loginfo(rospy.get_caller_id() +"Value: "+str(data.data))
        
    except Exception as e:
        print(data.data)
        print(e)

def listener():

    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('/arm_teleop/cam',Int32,callback)
    rospy.Subscriber('/arm_teleop/camA',Int32,callback2)
    rospy.Subscriber('/arm_teleop/joint5',Int32,callback3)
    rospy.spin()

if __name__ == '__main__':
    print("Enter main")
    kit = ServoKit(channels=16)
    servo_camArm = 7
    servo_camAntena = 2
    servo_rotacion = 6
    kit.servo[servo_camArm].set_pulse_width_range(500,2400)
    kit.servo[servo_camArm].actuation_range=180
    kit.servo[servo_camAntena].set_pulse_width_range(500,2400)
    kit.servo[servo_camAntena].actuation_range=180
    kit.servo[servo_rotacion].set_pulse_width_range(500,2500)
    kit.servo[servo_rotacion].actuation_range=642
    kit.servo[servo_camArm].angle=100
    kit.servo[servo_camAntena].angle=45
    kit.servo[servo_rotacion].angle=236

    listener()

