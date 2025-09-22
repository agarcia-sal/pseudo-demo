def process_special_text():
    # Step 1: Receive Input
    user_input = input().strip()  # Read input and remove leading/trailing whitespace

    # Step 2: Replace Text Representations
    user_input = user_input.replace("dot", ".").replace("at", "@")

    # Step 3: Initialize Variables
    count = 0
    characters = []

    # Step 4: Check and Adjust Starting Character for '.'
    if user_input.startswith("."):
        user_input = "dot" + user_input  # Prepend "dot" if first character is '.'

    # Step 5: Check and Adjust Starting Character for '@'
    if user_input.startswith("@"):
        user_input = "at" + user_input  # Prepend "at" if first character is '@'

    # Step 6: Process Each Character in the String
    for current_character in user_input:
        if current_character == '@':
            if count > 0:
                characters.append("at")
                count = 1  # Handle current "at"
            else:
                characters.append("@")
                count = 1  # First instance of @
        else:
            characters.append(current_character)  # Add current character to list

    # Step 7: Join Processed Characters
    final_string = ''.join(characters)

    # Step 8: Handle Trailing Periods
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"  # Replace last '.' with 'dot'

    # Step 9: Output the Final String
    print(final_string)  # Print the final result

# Call the function to execute
process_special_text()
