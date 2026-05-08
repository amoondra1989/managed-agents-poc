import time
import sys
from datetime import datetime

try:
    while True:
        now = datetime.now()
        # Clear the terminal screen
        sys.stdout.write('\033[2J\033[H')
        # Print the current time in DD:MM:YYYY HH:MM:SS format
        sys.stdout.write(now.strftime("%d:%m:%Y %H:%M:%S") + '\n')
        sys.stdout.flush()
        # Wait for one second
        time.sleep(1)
except KeyboardInterrupt:
    # Exit the program when Ctrl+C is pressed
    sys.exit()