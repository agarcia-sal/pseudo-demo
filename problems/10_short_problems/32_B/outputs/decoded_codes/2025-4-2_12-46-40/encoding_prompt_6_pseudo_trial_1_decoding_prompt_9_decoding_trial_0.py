def convert_dot_notation_to_number():
    # Read input from the user
    input_string = input()

    # Initialize index and output variable
    index = 0
    output_string = ''

    # Loop through the entire input string
    while index < len(input_string):
        # Check if the current character is a single dot
        if input_string[index] == '.':
            # Append '0' to the output for a single dot
            output_string += '0'
            # Move to the next character
            index += 1
        
        else: 
            # Check the next character to determine if it's a dot pair
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                # Append '1' to the output for a pair of dots
                output_string += '1'
                # Move the index forward by 2 characters
                index += 2
            
            else:
                # Append '2' for a dot followed by a non-dot
                output_string += '2'
                # Move the index forward by 2 characters
                index += 2
    
    # Output the final result
    print(output_string)

# To call the function, uncomment the following line:
# convert_dot_notation_to_number()
