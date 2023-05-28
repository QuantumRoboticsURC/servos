from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
kit.servo[4].set_pulse_width_range(500, 2400)
kit.servo[4].actuation_range=642
#kit.continuous_servo[2].throttle = 1
#kit.servo[8].angle = 130
kit.servo[4].angle = 90

