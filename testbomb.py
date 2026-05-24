import sys
import os
sys.setrecursionlimit(150000000)
bombobj = []
class oh:
    def __innit__(self,variable):
        self.variable = variable
def initialbomb():
    x = 1
    x+= 1
    y = 1
    y+=1
    for i in range(0,100000):
        os.system("python3 testbomb.py")
        initialbomb()
initialbomb()