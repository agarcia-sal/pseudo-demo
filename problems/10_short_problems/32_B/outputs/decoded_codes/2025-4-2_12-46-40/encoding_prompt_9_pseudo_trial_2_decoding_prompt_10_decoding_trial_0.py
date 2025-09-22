def convert_string_to_number(input_string):
    # Initialize variables
    currentIndex = 0
    outputString = ""

    # Process input string
    while currentIndex < len(input_string):
        # If the current character is a dot
        if input_string[currentIndex] == '.':
            outputString += '0'
            currentIndex += 1
        # If the current character is not a dot and the next character is a dot
        elif currentIndex + 1 < len(input_string) and input_string[currentIndex + 1] == '.':
            outputString += '1'
            currentIndex += 2
        # Otherwise, if neither is a dot
        else:
            outputString += '2'
            currentIndex += 2

    # Return the resulting numerical string
    return outputString

# Main function to run the program
if __name__ == "__main__":
    # Receive input
    user_input = input().strip()
    
    # Convert and output the result
    result = convert_string_to_number(user_input)
    print(result)
