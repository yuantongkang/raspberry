import RPI.GPIO
import time
import datetime
VCC1 = 7 
VCC2 = 8
A = 11
B = 12
C = 13
D = 15 
E = 16
F = 18
G = 21
DP = 22

def shownum0:
    GPIO.output(A,False)
    GPIO.output(B,False)
    GPIO.output(C,False)
    GPIO.output(D,False)
    GPIO.output(E,False)
    GPIO.output(F,False)
    GPIO.output(G,True)
    GPIO.output(DP,True)


shownum0()        