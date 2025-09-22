# Function to process a given string by replacing special text representations
def process_special_text():
    # 1. Receive Input
    user_input = input().strip()
    
    # 2. Replace Text Representations
    user_input = user_input.replace("dot", ".").replace("at", "@")

    # 3. Check and Adjust Starting Character
    if user_input.startswith("."):
        user_input = "dot " + user_input

    # 4. Initialize Variables
    count = 0
    characters = []

    # 5. Check for '@' Symbol at Start
    if user_input.startswith("@"):
        characters.append("at")
        count = 1

    # 6. Process Each Character in the String
    for current_character in user_input:
        if current_character == "@":
            if count > 0:
                # If an '@' was already counted, add 'at' instead
                characters.append("at")
                count = 1  # Reset count after handling
            else:
                characters.append("@")
                count = 1  # Indicate this '@' has been handled
        else:
            characters.append(current_character)
    
    # 7. Join Processed Characters
    final_string = ''.join(characters)

    # 8. Handle Trailing Periods
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # 9. Output the Final String
    print(final_string)

# Run the function to process the special text
process_special_text()
