import RPi.GPIO as GPIO

RPWM = 18
LPWM = 19

#Reversing the direction is unnecssary yk
GPIO.setup (RPWM, GPIO.OUT)
GPIO.setup (LPWM, GPIO.OUT)

#20kHz for quiet yet seamless speed control
pwm = GPIO.PWM(RPWM, 20000)
pwm.start(0)

def setSpeed (percent)
  pwm.ChangeDutyCycle(percent)
