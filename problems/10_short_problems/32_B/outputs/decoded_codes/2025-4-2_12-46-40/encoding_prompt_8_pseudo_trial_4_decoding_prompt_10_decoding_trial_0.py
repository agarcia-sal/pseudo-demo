def translate_encoding():
    # Read input and remove extra spaces/newlines
    input_string = input().strip()
    
    # Initialize variables
    current_position = 0
    result = ""
    
    # Process the input
    while current_position < len(input_string):
        if input_string[current_position] == '.':
            result += '0'  # Single dot translates to '0'
            current_position += 1  # Move one step forward
        elif current_position + 1 < len(input_string) and input_string[current_position + 1] == '.':
            result += '1'  # Pair of dots translates to '1'
            current_position += 2  # Move two steps forward
        else:
            result += '2'  # Sequence starting with a dash or otherwise translates to '2'
            current_position += 2  # Move two steps forward
    
    # Output the result
    print(result)

# Call the function to execute
translate_encoding()
