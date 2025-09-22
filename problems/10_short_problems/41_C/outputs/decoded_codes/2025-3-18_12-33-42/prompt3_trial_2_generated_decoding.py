# Function to process the input string according to specified rules
def process_input_string():
    # Read input from the user
    input_string = input()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')
    
    # Check if the first character is a dot and prepend 'dot' if needed
    if input_string.startswith('.'):
        input_string = 'dot' + input_string
    
    # Initialize variables for processing
    consecutive_at_count = 0
    result_string = []  # Using a list to collect characters
     
    # Check if the first character is an at symbol and prepend 'at' if needed
    if input_string.startswith('@'):
        input_string = 'at' + input_string
    
    # Iterate over each character in the input string
    for character in input_string:
        if character == '@':
            # If the current character is an '@'
            if consecutive_at_count > 0:
                result_string.append('at')
                consecutive_at_count = 1  # Reset the count to 1
            else:
                result_string.append('@')
                consecutive_at_count = 1  # Start counting consecutive '@'
        else:
            # If the current character is not '@'
            result_string.append(character)
            consecutive_at_count = 0  # Reset the count for non '@' characters
    
    # Join the result list back into a string
    final_string = ''.join(result_string)
    
    # Check if the last character of resulting string is a dot
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'
    
    # Output the final modified string
    print(final_string)

# Call the function to execute the code
process_input_string()
