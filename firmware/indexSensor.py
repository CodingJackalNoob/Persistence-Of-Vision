"""Every revolution notes down an absolute angle ref, interpolating the rest, allowing for
time synchronization.
"""
import Rpi.GPIO as GPIO

INDEX_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(INDEX_PIN, GPIO.IN)

def waitForIndex():
  GPIO.wait_for_edge(INDEX_PIN, GPIO.FALLING)
