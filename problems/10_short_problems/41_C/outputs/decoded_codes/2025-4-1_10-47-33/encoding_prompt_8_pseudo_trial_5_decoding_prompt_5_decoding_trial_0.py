def convert_to_email_format():
    # Step 1: Read input from user and trim whitespace
    input_string = input().strip()

    # Step 2: Replace "dot" and "at" with their symbols
    input_string = input_string.replace("dot", ".").replace("at", "@")

    # Step 3: Handle leading character case
    if input_string.startswith("."):
        input_string = "dot" + input_string

    # Step 4: Initialize variables
    occurrences_of_at = 0
    final_output = []

    # Step 5: Correct leading "at"
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]

    # Step 6: Process each character of the modified string
    for character in input_string:
        if character == "@":
            if occurrences_of_at > 0:
                final_output.append("at")  # Append "at" for additional occurrences
            else:
                final_output.append("@")  # Append "@" for the first occurrence
            occurrences_of_at += 1
        else:
            final_output.append(character)  # Append other characters directly

    # Step 7: Create final output string
    final_string = ''.join(final_output)

    # Step 8: Replace trailing dot, if applicable
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"  # Replace last character with "dot"

    # Step 9: Output the result
    print(final_string)

# Example usage
convert_to_email_format()
