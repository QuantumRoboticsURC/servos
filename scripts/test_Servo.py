from adafruit_servokit import ServoKit
if __name__ == '__main__':
    kit = ServoKit(channels=16)
    servo_cero = 6
    kit.servo[servo_cero].set_pulse_width_range(500, 2500)
    kit.servo[servo_cero].actuation_range = 642

    while True: 
        try: 
            angle = int(input("Ingrese el ángulo: "))
            kit.servo[servo_cero].angle=angle
            print(kit.servo[servo_cero].angle)
            kill = int(input("Ingrese 1 si quiere matar el código: "))
            if(kill==1):
               break
        except: 
            print("Error")
