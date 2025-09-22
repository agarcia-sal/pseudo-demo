# Function to convert the input string according to the specified logic
def convert_string():
    # Read input string from standard input
    input_string = input()
    
    # Initialize index and output variable
    index = 0
    output_string = ''

    # Loop through the input string until the end
    while index < len(input_string):
        # Check if the current character is '.'
        if input_string[index] == '.':
            # Append '0' to the output
            output_string += '0'
            # Move to the next character
            index += 1
            
        # Check for the pattern ".."
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' to the output
            output_string += '1'
            # Move the index forward by two characters
            index += 2
            
        # Default condition for patterns like '.-' or other characters
        else:
            # Append '2' to the output
            output_string += '2'
            # Move the index forward by two characters
            index += 2

    # Output the final result
    print(output_string)

# Call the function to execute
convert_string()
