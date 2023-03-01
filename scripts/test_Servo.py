from adafruit_servokit import ServoKit
if __name__ == '__main__':
    kit = ServoKit(channels=16)
    servo_cero = 4

    while True: 
        try: 
            angle = int(input("Ingrese el ángulo: "))
            kit.servo[servo_cero].set_pulse_width_range(1000, 2000)
            kit.servo[servo_cero].actuation_range = 180
            kit.servo[servo_cero].angle=angle
            print(kit.servo[servo_cero].angle)
        except: 
            print("Error")
