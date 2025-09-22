def process_input_string():
    # Read input from standard input and remove leading/trailing whitespace
    input_string = input().strip()
    
    # Initialize index and result variable
    index = 0
    result = ""
    
    # Process each character in the input string
    while index < len(input_string):
        # Check if the current character is a period
        if input_string[index] == '.':
            result += '0'
            index += 1
        else:
            # Check if there is a next character
            if index + 1 < len(input_string):
                # Check if the next character is a period
                if input_string[index + 1] == '.':
                    result += '1'
                    index += 2  # Move the index forward by 2
                else:
                    result += '2'
                    index += 2  # Move the index forward by 2
            else:
                # If there's no next character but current is not a period
                result += '2'
                index += 1  # Move the index forward by 1 if we're at the last character

    # Output the final result
    print(result)

# Call the function
process_input_string()
