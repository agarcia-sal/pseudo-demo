def process_input_string():
    # Read input from standard input and strip leading/trailing whitespace
    input_string = input().strip()
    
    # Initialize index and result variable
    index = 0
    result = ""

    # Process each character in the input string
    while index < len(input_string):
        # Check if the current character is a period
        if input_string[index] == '.':
            # Append '0' to the result
            result += '0'
            # Move the index to the next character
            index += 1
        else:
            # Check the next character if it exists
            if index + 1 < len(input_string):
                # Check if the next character is a period
                if input_string[index + 1] == '.':
                    # Append '1' to the result
                    result += '1'
                    # Move the index forward by 2
                    index += 2
                else:
                    # If neither character is a period
                    # Append '2' to the result
                    result += '2'
                    # Move the index forward by 2
                    index += 2
            else:
                # If we reach the end of the string with no next character, append '2'
                result += '2'
                index += 1

    # Output the final result
    print(result)

# Call the function to execute
process_input_string()
