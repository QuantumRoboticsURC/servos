import rospy
from lab_arm.msg import arm_lab,joint1,joint2
from adafruit_servokit import ServoKit
import time

def callback():
    global servo_center,servo_left,servo_right,joint3_b
    lab = arm_lab()
    kit.servo[servo_left].angle=lab.servo1
    kit.servo[servo_center].angle=lab.servo2
    kit.servo[servo_right].angle=lab.servo3
    kit.servo[joint3_b].angle=lab.joint3

def servo_listener():
    rospy.init_node('lab_servos',anonymous=True)
    rospy.Subscriber('arm_lab',arm_lab,callback)
    rospy.spin()

if __name__ == '__main__':
    kit = ServoKit(channels=16)
    servo_left = 4
    servo_center = 5
    servo_right = 6
    joint3_b = 7
    kit.servo[servo_left].actuation_range=180
    kit.servo[servo_center].actuation_range=180
    kit.servo[servo_right].actuation_range=180
    kit.servo[joint3_b].actuation_range=642
    kit.servo[servo_left].set_pulse_width_range(1000,2000)
    kit.servo[servo_center].set_pulse_width_range(1000,2000)
    kit.servo[servo_right].set_pulse_width_range(1000,2000)
    kit.servo[joint3_b].set_pulse_width_range(500,2500)

    servo_listener()