def process_special_text():
    # Step 1: Receive Input
    user_input = input().strip()

    # Step 2: Replace Text Representations
    user_input = user_input.replace("dot", ".")
    user_input = user_input.replace("at", "@")

    # Step 3: Check and Adjust Starting Character
    if user_input.startswith('.'):
        user_input = "dot" + user_input

    # Step 4: Initialize Variables
    count = 0
    characters = []

    # Step 5: Check for '@' Symbol at Start
    if user_input.startswith("@"):
        user_input = "at" + user_input
    
    # Step 6: Process Each Character in the String
    for current_character in user_input:
        if current_character == "@":
            if count > 0:
                # Adding "at" representation if we have previously counted "at"
                characters.append("at")
                count = 1  # Reset count
            else:
                characters.append("@")
                count = 1  # Set count to indicate "at" has been added
        else:
            characters.append(current_character)
    
    # Step 7: Join Processed Characters
    final_string = ''.join(characters)

    # Step 8: Handle Trailing Periods
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"

    # Step 9: Output the Final String
    print(final_string)

# Example usage (please uncomment the line below to test the function):
# process_special_text()
