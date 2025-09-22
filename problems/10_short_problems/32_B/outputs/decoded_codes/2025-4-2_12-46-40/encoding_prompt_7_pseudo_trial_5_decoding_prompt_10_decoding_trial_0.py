def convert_input_to_binary_string():
    # Read input string from standard input
    input_string = input()
    
    # Initialize index for traversing the input string
    index = 0
    # Initialize an empty result string
    result_string = ""
    
    # Traverse the input string
    while index < len(input_string):
        if input_string[index] == '.':
            # If the current character is '.', append '0'
            result_string += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If the next character is also '.', append '1'
            result_string += '1'
            index += 2
        else:
            # Append '2' for any other case (which means '.' is not present)
            result_string += '2'
            index += 2
    
    # Print the final result string
    print(result_string)

# Call the function to execute
convert_input_to_binary_string()
