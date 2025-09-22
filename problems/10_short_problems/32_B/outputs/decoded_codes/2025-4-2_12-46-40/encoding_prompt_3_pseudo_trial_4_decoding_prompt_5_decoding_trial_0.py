# Function to process the input string based on dot patterns
def process_dots():
    # Read input string and remove leading and trailing whitespace
    string_input = input().strip()
    
    # Initialize variables
    current_index = 0
    result_string = ""

    # Process the input string
    while current_index < len(string_input):
        if string_input[current_index] == '.':
            # Append '0' for a single dot
            result_string += '0'
            current_index += 1
        elif current_index + 1 < len(string_input) and string_input[current_index + 1] == '.':
            # Append '1' for two consecutive dots
            result_string += '1'
            current_index += 2
        else:
            # Append '2' if the next character is not a dot or if it's the last character
            result_string += '2'
            current_index += 2

    # Output the result
    print(result_string)

# Example test case (uncomment to test)
# process_dots() # If the input is "..xy", the output should be "12"
