def convert_input_to_output():
    # Read input from the user and strip unnecessary spaces
    user_input = input().strip()
    index = 0
    result = ""

    # Loop through the input string until the end is reached
    while index < len(user_input):
        # Check if the current character is a dot
        if user_input[index] == '.':
            result += '0'  # Append '0' to result
            index += 1
        else:
            # Check the next character after the current one
            if index + 1 < len(user_input) and user_input[index + 1] == '.':
                result += '1'  # Append '1' to result
                index += 2
            else:
                result += '2'  # Append '2' to result
                index += 2

    # Output the resulting string
    print(result)

# This represents the main flow of the program
convert_input_to_output()
