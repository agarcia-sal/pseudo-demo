def convert_input_to_output():
    # Get input from the user and strip unnecessary spaces
    user_input = input().strip()
    index = 0  # Initialize index to track position in the string
    result = ""  # Initialize an empty string for the result
    
    # Loop through the input string until the end is reached
    while index < len(user_input):
        # Check if the current character is a dot
        if user_input[index] == '.':
            result += '0'  # Append '0' to result
            index += 1  # Increment index by 1
        else:
            # Check the next character after the current one
            if index + 1 < len(user_input) and user_input[index + 1] == '.':
                result += '1'  # Append '1' to result
                index += 2  # Increment index by 2
            else:
                result += '2'  # Append '2' to result
                index += 2  # Increment index by 2

    # Output the resulting string
    print(result)

# Call the function to execute the program
convert_input_to_output()
