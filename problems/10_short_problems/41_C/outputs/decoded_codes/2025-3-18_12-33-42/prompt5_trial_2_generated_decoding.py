# Function to convert user input into email-like format
def format_email():
    # Input the string and remove leading/trailing whitespace
    user_input = input().strip()
    
    # Replace specified words with their respective symbols
    user_input = user_input.replace("dot", ".")
    user_input = user_input.replace("at", "@")
    
    # Special case: If the first character is a ".", prepend "dot"
    if user_input.startswith("."):
        user_input = "dot" + user_input
    
    # Initialize tracking variables
    at_count = 0
    final_parts = []

    # Special case: If the first character is "@", prepend "at"
    if user_input.startswith("@"):
        user_input = "at" + user_input

    # Process each character in the string
    for character in user_input:
        if character == "@":
            if at_count > 0:
                # If "@" has appeared before, append "at" to final_parts
                final_parts.append("at")
            else:
                # If first occurrence of "@", append it normally
                final_parts.append("@")
            at_count += 1  # Track that "@" has been encountered
        else:
            # Append the character to final_parts
            final_parts.append(character)
    
    # Join final_parts into a single output string
    output_string = ''.join(final_parts)
    
    # Check for trailing periods
    if output_string.endswith("."):
        # Replace last character with "dot"
        output_string = output_string[:-1] + "dot"

    # Output the final string
    print(output_string)

# Example use case (can be tested using comments):
# format_email()  # User can provide input in this manner
