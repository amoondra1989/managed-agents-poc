import time
import sys
import random
from datetime import datetime

try:
    while True:
        now = datetime.now()
        # Clear the terminal screen
        sys.stdout.write('\033[2J\033[H')
        # Generate random x and y positions
        x_pos = random.randint(0, 20)  # Assuming terminal height 20
        y_pos = random.randint(0, 40)  # Assuming terminal width 40
        # Move the cursor to a random position
        sys.stdout.write(f'\033[{x_pos};{y_pos}H')
        # Print the current time in DD:MM:YYYY HH:MM:SS format
        sys.stdout.write(now.strftime("%d:%m:%Y %H:%M:%S") + '\n')
        sys.stdout.flush()
        # Wait for one second
        time.sleep(1)
except KeyboardInterrupt:
    # Exit the program when Ctrl+C is pressed
    sys.exit()