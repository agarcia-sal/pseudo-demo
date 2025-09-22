# Function to modify input string according to specific rules
def modify_string():
    # Step 1: Receive Input
    input_string = input().strip()

    # Step 2: Replace Specific Strings
    modified_string = input_string.replace("dot", ".").replace("at", "@")

    # Step 3: Check Beginning of String
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string[1:]

    # Step 4: Initialize Variables
    at_counter = 0  # Counter for "at" occurrences
    collected_characters = []  # List to collect characters

    # Step 5: Handle Starting Character
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]

    # Step 6: Iterate Through Characters
    for char in modified_string:
        if char == "@":
            if at_counter > 0:  # If "at" has occurred before
                collected_characters.append("at")
            else:  # First occurrence of "@"
                collected_characters.append("@")
            at_counter += 1
        else:
            collected_characters.append(char)

    # Step 7: Combine Collected Characters
    final_string = ''.join(collected_characters)

    # Step 8: Final Adjustment
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"  # Replace last character with "dot"

    # Step 9: Output the Result
    print(final_string)

# Example usage and testing should be done outside this function
