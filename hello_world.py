import sys
import random

# List of preconfigured names
names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

# Check if name is provided as a command-line argument
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = random.choice(names)

# Print the greeting message
print(f'Hello {name}, How are you today?')
