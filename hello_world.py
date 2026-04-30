# This script prints Hello followed by a name provided as an argument, defaults to 'Abhishek'
import sys

def main():
    # Check if a name was provided as an argument
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Abhishek"
    
    print(f'Hello {name}')

if __name__ == "__main__":
    main()
