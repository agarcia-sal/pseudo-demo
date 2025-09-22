# Function to process the input string according to defined rules
def process_string():
    # Read a line of text from standard input
    input_string = input()
    
    # Replace keywords in the input string
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")

    # Handle special case for the first character
    if input_string.startswith("."):
        input_string = "dot" + input_string[1:]

    # Initialize variables
    at_count = 0  # Count occurrences of "@"
    result_list = []  # List to collect processed characters and strings

    # Handle special case for email format
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]

    # Process each character in the input string
    for current_char in input_string:
        if current_char == "@":
            if at_count > 0:
                result_list.append("at")  # Append "at" for additional occurrences
            else:
                result_list.append("@")  # Append the first occurrence of "@"
            at_count = 1  # Set count to indicate we've seen an "@"
        else:
            result_list.append(current_char)  # Append other characters

    # Combine results into a single string
    output_string = ''.join(result_list)

    # Handle ending special case
    if output_string.endswith("."):
        output_string = output_string[:-1] + "dot"  # Replace last "." with "dot"

    # Output the final result
    print(output_string)

# Call the function to execute
process_string()
