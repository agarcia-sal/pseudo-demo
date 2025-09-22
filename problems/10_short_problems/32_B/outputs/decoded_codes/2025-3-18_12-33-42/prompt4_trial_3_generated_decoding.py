def transform_input_string():
    # Read input string from the standard input
    input_string = input()

    # Initialize index and result variable
    index = 0
    result = ""

    # Loop through the input string until the end is reached
    while index < len(input_string):
        # Check for the first character
        if input_string[index] == '.':
            # If current character is '.', append '0' to result
            result += "0"
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If the next character is also '.', append '1' to result
            result += "1"
            index += 2  # Move past the current and next character
        else:
            # If neither case fits, append '2' to result
            result += "2"
            index += 2  # Move past the current and next character

    # Print the final result
    print(result)

# Call the function to execute the code
transform_input_string()
