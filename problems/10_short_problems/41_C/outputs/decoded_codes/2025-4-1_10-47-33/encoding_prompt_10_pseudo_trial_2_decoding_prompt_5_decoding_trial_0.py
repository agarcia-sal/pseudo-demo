# Function to process the input string
def process_string():
    # Read input string and trim whitespace
    input_string = input().strip()
    
    # Replace "dot" with "." and "at" with "@"
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")
    
    # Prepend "dot" if the first character is a period
    if input_string and input_string[0] == '.':
        input_string = "dot" + input_string[1:]
    
    # Initialize variables for processing
    count_at = 0
    result_list = []

    # Prepend "at" if the first character is an "@" but not empty
    if input_string and input_string[0] == '@':
        result_list.append("at")
        input_string = input_string[1:]

    # Process each character in the string
    for character in input_string:
        if character == '@':
            if count_at > 0:
                result_list.append("at")  # Append "at" instead of "@" if it already appeared
            else:
                result_list.append("@")  # Append "@" directly
            count_at = 1
        else:
            result_list.append(character)  # Append the character if it's not "@"

    # Join the processed characters into a single output string
    processed_string = ''.join(result_list)

    # Replace the last character with "dot" if it is a period
    if processed_string and processed_string[-1] == '.':
        processed_string = processed_string[:-1] + "dot"
    
    # Output the final processed string
    print(processed_string)

# Example test case (not to be included in the final code)
# For testing purposes, you can uncomment the following line:
# process_string()
