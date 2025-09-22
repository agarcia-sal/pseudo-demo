# Start the Program
def process_input_string():
    # Read Input
    input_string = input().strip()

    # Initialize Variables
    index = 0
    result = ""

    # Process the Input String
    while index < len(input_string):
        if input_string[index] == '.':
            # If the character at the current index is a dot
            result += '0'  # Append '0' to result
            index += 1     # Increment index to move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If the next character is also a dot
            result += '1'  # Append '1' to result
            index += 2     # Increment index by 2 to skip the next character
        else:
            # For any other character
            result += '2'  # Append '2' to result
            index += 2     # Increment index by 2 to skip the next character

    # Output the Result
    print(result)

# Invoke the function to run the program
process_input_string()
