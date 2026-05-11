import sys
import random
import time

# List of preconfigured names
names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

# Check if name is provided as a command-line argument
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = random.choice(names)

# Sleep for 10 seconds
time.sleep(10)

# Print the greeting message
print(f'Hello {name}, How are you today?')
