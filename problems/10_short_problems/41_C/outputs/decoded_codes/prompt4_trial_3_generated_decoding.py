def process_email(input_string):
    # Read the input string and remove any surrounding whitespace
    cleaned_input = input_string.strip()
    
    # Replace instances of 'dot' with '.' and 'at' with '@'
    cleaned_input = cleaned_input.replace("dot", ".")
    cleaned_input = cleaned_input.replace("at", "@")
    
    # Check if the first character is a '.' and prepend 'dot' if it is
    if cleaned_input and cleaned_input[0] == '.':
        cleaned_input = "dot" + cleaned_input[1:]

    # Initialize a counter for '@' instances and an empty list for final characters
    count_at_symbols = 0
    final_characters = []
    
    # Check if the first character is an '@' and prepend 'at' if it is
    if cleaned_input and cleaned_input[0] == '@':
        cleaned_input = "at" + cleaned_input[1:]

    # Iterate over each character in the cleaned input
    for character in cleaned_input:
        if character == '@':
            # If we've already encountered an '@', append 'at' instead of '@'
            if count_at_symbols > 0:
                final_characters.append("at")
                count_at_symbols = 1
            else:
                final_characters.append('@')
                count_at_symbols += 1
        else:
            final_characters.append(character)

    # Join the characters into a single string
    final_string = ''.join(final_characters)

    # If the last character is a '.', replace it with 'dot'
    if final_string and final_string[-1] == '.':
        final_string = final_string[:-1] + "dot"

    # Output the final processed string
    print(final_string)

# Example usage (you can comment this out in actual implementation)
# process_email(input())
