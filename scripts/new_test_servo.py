from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
kit.servo[7].set_pulse_width_range(500, 2400)
kit.servo[7].actuation_range=180
#kit.continuous_servo[2].throttle = 1
kit.servo[7].angle = 90
