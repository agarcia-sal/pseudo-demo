# Define the main function to process the input string
def main():
    # Read input string from standard input and remove unnecessary whitespace
    input_string = input().strip()
    
    # Initialize an index to track current position in the string
    index = 0
    
    # Initialize an empty string to build the output
    output = ""
    
    # Continue processing the input string until the whole string is examined
    while index < len(input_string):
        # Check for the current character
        if input_string[index] == '.':
            # If current character is '.', add '0' to output and move to next character
            output += '0'
            index += 1
        else:
            # Check the next character in the string
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                # If the next character is also '.', add '1' to output and move ahead by two characters
                output += '1'
                index += 2
            else:
                # If neither of the two characters is '.', add '2' to output and move ahead by two characters
                output += '2'
                index += 2
    
    # Output the final constructed string
    print(output)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
