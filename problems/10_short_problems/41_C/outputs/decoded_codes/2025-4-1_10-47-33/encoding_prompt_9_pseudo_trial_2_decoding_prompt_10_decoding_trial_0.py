def process_special_text():
    # Step 1: Receive Input
    user_input = input().strip()  # remove leading/trailing whitespace

    # Step 2: Replace Text Representations
    user_input = user_input.replace("dot", ".").replace("at", "@")

    # Step 3: Check and Adjust Starting Character
    if user_input.startswith("."):
        user_input = "dot" + user_input  # prepend "dot" if line starts with "."

    # Step 4: Initialize Variables
    count = 0
    characters = []

    # Step 5: Check for '@' Symbol at Start
    if user_input.startswith("@"):
        characters.append("at")  # prepend "at" if line starts with "@"
        count = 1

    # Step 6: Process Each Character in the String
    for current_character in user_input:
        if current_character == "@":
            if count > 0:
                characters.append("at")
                count = 1  # maintain the count when handling subsequent "at"
            else:
                characters.append("@")
                count = 1
        else:
            characters.append(current_character)
    
    # Step 7: Join Processed Characters
    final_string = ''.join(characters)

    # Step 8: Handle Trailing Periods
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"  # Replace last "." with "dot"

    # Step 9: Output the Final String
    print(final_string)

# Optional: Call the function to execute
process_special_text()
