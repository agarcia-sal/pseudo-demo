# Function to process input string and generate output string based on specific rules
def process_dots_and_dashes():
    # Read input from standard input and remove any leading/trailing whitespace
    input_string = input().strip()

    # Initialize variables
    index = 0
    output_string = ''

    # Process the input string while we haven't reached the end
    while index < len(input_string):
        # Check current character at the index
        if input_string[index] == '.':
            # Add '0' to output_string for a single dot
            output_string += '0'
            # Move to the next character
            index += 1
            
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Add '1' to output_string for two consecutive dots
            output_string += '1'
            # Move index forward by two characters
            index += 2
        
        else:
            # Add '2' to output_string for a dash followed by any character
            output_string += '2'
            # Move index forward by two characters
            index += 2

    # Output the final result
    print(output_string)

# Execute the function to run the code
process_dots_and_dashes()
