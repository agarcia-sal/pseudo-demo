def convert_dots_to_numbers():
    # Read input string from standard input
    input_string = input()
    
    # Initialize index and result string
    index = 0
    result = ''
    
    # Loop until all characters in the string have been processed
    while index < len(input_string):
        if input_string[index] == '.':
            # Append '0' to the result for a single dot
            result += '0'
            index += 1
        elif index < len(input_string) - 1 and input_string[index + 1] == '.':
            # Append '1' to the result for a dot followed by a dot
            result += '1'
            index += 2
        else:
            # Append '2' for any other scenario (dot followed by something else)
            result += '2'
            index += 2
            
    # Output the result string
    print(result)

# Call the function to execute
convert_dots_to_numbers()
