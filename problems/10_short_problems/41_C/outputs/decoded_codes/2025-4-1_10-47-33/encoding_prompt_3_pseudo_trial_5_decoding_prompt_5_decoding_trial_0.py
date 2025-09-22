# Function to process the input string based on specified rules
def process_input_string():
    # Read input from the user
    input_string = input().strip()  # Remove surrounding whitespace

    # Replace occurrences of "dot" with "." and "at" with "@"
    input_string = input_string.replace("dot", ".").replace("at", "@")

    # Ensure that the string starts with "dot" if it begins with '.'
    if input_string.startswith('.'):
        input_string = "dot" + input_string[1:]

    # Initialize variables for processing
    consecutive_at_count = 0
    result_characters = []

    # If the string starts with '@', prefix it with "at"
    if input_string.startswith('@'):
        input_string = "at" + input_string[1:]

    # Iterate through each character in the input_string
    for character in input_string:
        if character == '@':
            if consecutive_at_count > 0:
                result_characters.append("at")  # Append "at" for consecutive '@'
                consecutive_at_count = 1  # Reset count
            else:
                result_characters.append("@")  # Append just '@'
                consecutive_at_count = 1  # Increment count
        else:
            result_characters.append(character)  # Append regular characters

    # Join the characters back into a single string
    output_string = ''.join(result_characters)

    # If the last character of output_string is '.', replace it with 'dot'
    if output_string.endswith('.'):
        output_string = output_string[:-1] + "dot"  # Replace '.' with 'dot'

    # Display the final output
    print(output_string)

# Test the function
# process_input_string()  # Uncomment this line to run the function and provide input during execution
