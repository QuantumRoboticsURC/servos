#!usr/bin/env python3
import rospy
from servos.msg import arm_lab
from adafruit_servokit import ServoKit
import time
from std_msgs.msg import Int32 
def callback(lab):
    global servo_center,servo_left,servo_right,joint3_b
    print(lab)
    #kit.servo[servo_left].angle=lab.servo1
    #kit.servo[servo_center].angle=lab.servo2
    #kit.servo[servo_right].angle=lab.servo3
    kit.servo[joint3_b].angle=lab.data

def callback2(lab):
    global servo_right
    print("AAAAAAAAA")
    print(lab)
    kit.servo[servo_right].angle=lab.data
def callback3(lab):
    global servo_center
    print("AAAAAAAAA")
    print(lab)
    kit.servo[servo_center].angle=lab.data
def callback4(lab):
    global servo_left
    print("AAAAAAAAA")
    print(lab)
    kit.servo[servo_left].angle=lab.data

def servo_listener():
    rospy.init_node('lab_servos',anonymous=True)
    rospy.Subscriber('/arm_lab/joint3',Int32,callback)
    rospy.Subscriber('/servo_right',Int32,callback2)   
    rospy.Subscriber('/servo_center',Int32,callback3)
    rospy.Subscriber('/servo_left',Int32,callback4)      
    rospy.spin()

if __name__ == '__main__':
    kit = ServoKit(channels=16)
    servo_left = 8
    servo_center = 7
    servo_right = 5
    joint3_b = 4
    kit.servo[servo_left].actuation_range=180
    kit.servo[servo_center].actuation_range=180
    kit.servo[servo_right].actuation_range=180
    kit.servo[joint3_b].actuation_range=642
    kit.servo[servo_left].set_pulse_width_range(1000,2000)
    kit.servo[servo_center].set_pulse_width_range(1000,2000)
    kit.servo[servo_right].set_pulse_width_range(1000,2000)
    kit.servo[joint3_b].set_pulse_width_range(500,2500)

    servo_listener()
