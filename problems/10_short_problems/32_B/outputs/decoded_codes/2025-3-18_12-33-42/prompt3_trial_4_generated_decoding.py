# Define the function to process the input sequence
def process_input_sequence():
    # Read input from standard input
    input_sequence = input()
    index = 0  # Initialize index to traverse the input
    output_string = ""  # Initialize output string

    # Loop through the input string until all characters are processed
    while index < len(input_sequence):
        if input_sequence[index] == '.':
            # Append '0' for a single '.'
            output_string += '0'
            index += 1  # Move to the next character
        else:
            # Check the next character in the sequence
            if index + 1 < len(input_sequence) and input_sequence[index + 1] == '.':
                # Append '1' for the pattern '..'
                output_string += '1'
                index += 2  # Move past the two characters
            else:
                # Append '2' for the pattern '.-' or similar
                output_string += '2'
                index += 2  # Move past the two characters

    # Print the final output string
    print(output_string)

# Call the function to execute
process_input_sequence()
