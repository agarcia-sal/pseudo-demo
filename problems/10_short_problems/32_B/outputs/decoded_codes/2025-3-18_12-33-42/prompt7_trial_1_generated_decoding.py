def decode_input(input_string):
    # Initialize an index to traverse the input string
    index = 0
    # Initialize an empty string to accumulate the result
    result = ""

    # Loop through the input string until the end is reached
    while index < len(input_string):
        # Check for the current character
        if input_string[index] == '.':
            # If character is '.', append '0' to result
            result += '0'
            # Move to the next character
            index += 1
            
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If the next character is '.', append '1' to result
            result += '1'
            # Move index forward by 2 characters
            index += 2
            
        else: 
            # Otherwise, append '2' to result
            result += '2'
            # Move index forward by 2 characters
            index += 2
            
    # Output the final result
    return result

# Main Execution
input_string = input()  # Read input from standard input
result = decode_input(input_string)  # Call the decode function
print(result)  # Print the result from the decoding function
