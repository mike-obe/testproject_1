import time
import os

with open("test.txt") as f:
    for line in f:
        print time.time(), line
