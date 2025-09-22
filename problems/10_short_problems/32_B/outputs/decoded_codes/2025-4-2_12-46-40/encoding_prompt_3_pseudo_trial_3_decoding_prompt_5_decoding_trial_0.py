# Function to process the input string according to specified rules
def process_string():
    # Read input string from standard input
    received_string = input()

    # Initialize index for string traversal
    current_index = 0
    # Initialize an empty string to store the result
    result_string = ''

    # Loop through the input string while the current index is within bounds
    while current_index < len(received_string):
        # Check if the current character is a dot (.)
        if received_string[current_index] == '.':
            # Append '0' to the result string
            result_string += '0'
            # Move to the next character
            current_index += 1
        # Check if the next character is a dot (.)
        elif current_index + 1 < len(received_string) and received_string[current_index + 1] == '.':
            # Append '1' to the result string
            result_string += '1'
            # Move the index forward by two characters
            current_index += 2
        # Otherwise, process the character as a different case
        else:
            # Append '2' to the result string
            result_string += '2'
            # Move the index forward by two characters
            current_index += 2

    # Output the final result string
    print(result_string)

# Uncomment the following line to run the function when the script is executed
# process_string()
