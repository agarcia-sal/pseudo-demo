def format_string():
    # Step 1: Read the input string and prepare it for processing
    input_string = input().strip()  # Read input and remove leading/trailing whitespace

    # Step 2: Replace specific substrings for formatting
    input_string = input_string.replace("dot", ".").replace("at", "@")

    # Step 3: Check and modify the first character if it's a period
    if input_string.startswith("."):
        input_string = "dot" + input_string[1:]  # Prepend "dot" to the string

    # Step 4: Initialize variable for processing
    count_at = 0  # Counter for occurrences of '@'
    formatted_characters = []  # List to hold processed characters

    # Step 5: Modify the string further if it starts with '@'
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]  # Prepend "at" to the string

    # Step 6: Iterate through each character in the modified string
    for char in input_string:
        if char == "@":
            if count_at > 0:
                formatted_characters.append("at")  # Append "at" if it's not the first occurrence
            else:
                formatted_characters.append("@")  # Append "@" for the first occurrence
            count_at += 1  # Increment count_at after handling '@'
        else:
            formatted_characters.append(char)  # Append other characters as-is

    # Step 7: Join the formatted characters into a single string
    output_string = ''.join(formatted_characters)

    # Step 8: Final formatting for the output string
    if output_string.endswith("."):
        output_string = output_string[:-1] + "dot"  # Replace the last character with "dot"

    # Step 9: Output the final formatted string
    print(output_string)

# Example invocation (this would be done elsewhere in practice):
# format_string()
