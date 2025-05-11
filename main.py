import os
import random
import shutil
import sys

def is_elevated():
    #Unix check
    if hasattr(os, "getuid"):
        return os.getuid() == 0
    
    #Windows Check
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False
    
if not is_elevated():
    sys.exit("Script must be run with root/admin")

choices= ["heads", "tails"]

print("Let's play a game!")
answer= "0"
while True:
    answer= input("Heads or tails: ").lower().strip()
    if answer in choices:
        break
    print("Try again")

if (answer== random.choice(choices)):
    print("You lose")
else:
    print("You win")