# Function to process the input string according to specified rules
def process_dots():
    # Read input from user
    input_string = input().strip()

    # Initialize index and the answer string
    current_index = 0
    result_string = ''

    # Process the input string until the end
    while current_index < len(input_string):
        # Check for conditions based on characters in the input string
        if input_string[current_index] == '.':
            # Add '0' to the result for a single dot
            result_string += '0'
            current_index += 1
        
        elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            # Add '1' to the result for two consecutive dots
            result_string += '1'
            current_index += 2
        
        else:
            # Handle other cases (e.g., when next character isn't a dot)
            result_string += '2'
            current_index += 2
    
    # Output the resulting string
    print(result_string)

# Call the function to execute the code
process_dots()
