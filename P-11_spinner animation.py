''' Write a Python program to display a rotating console cursor (spinner animation: |, /, -, \) on 
the command-line terminal that runs for a set time duration.'''

import sys
import time

def spin_for(seconds):
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + seconds
    i = 0
    
    while time.time() < end_time:
        sys.stdout.write(f'\rLoading {spinner[i]}')
        sys.stdout.flush()
        time.sleep(0.1)
        i = (i + 1) % len(spinner)
        
    sys.stdout.write('\rDone!          \n')

if __name__ == '__main__':
    spin_for(5)
