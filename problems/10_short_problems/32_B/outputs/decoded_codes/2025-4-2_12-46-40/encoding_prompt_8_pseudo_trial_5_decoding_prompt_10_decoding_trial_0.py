# Importing necessary libraries
import sys

def main():
    # Read a single line of input and remove any extra spaces
    input_string = input().strip()

    # Initialize variables
    index = 0
    result = ""

    # Process the input string
    while index < len(input_string):
        if input_string[index] == '.':
            result += '0'  # Translate '.' to '0'
            index += 1      # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'  # Translate '..' to '1'
            index += 2      # Skip both characters
        else:
            result += '2'  # Translate any other character to '2'
            index += 2      # Skip both characters

    # Output the result
    print(result)

# Entry point of the program
if __name__ == "__main__":
    main()
