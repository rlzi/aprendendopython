import time
from colorama import Fore, init, Style

init()

for i in range(101):
    print(f"\rPROGRESSO: {i}%", end="")
    time.sleep(0.1)