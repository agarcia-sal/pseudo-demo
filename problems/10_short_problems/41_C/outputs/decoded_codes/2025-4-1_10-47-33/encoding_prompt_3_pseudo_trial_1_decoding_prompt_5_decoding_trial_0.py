# Function to format an input string based on specific character replacements and rules
def format_string():
    # Step 1: Read the input string and prepare it for processing
    input_string = input().strip()  # Removing leading/trailing whitespace

    # Step 2: Replace specific substrings for formatting
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")

    # Step 3: Check and modify the first character if it's a period
    if input_string and input_string[0] == ".":
        input_string = "dot" + input_string[1:]

    # Step 4: Initialize variables for processing the string
    count_at = 0  # Counter for occurrences of '@' character
    formatted_characters = []  # To hold processed characters

    # Step 5: Modify the string further if it starts with '@'
    if input_string and input_string[0] == "@":
        input_string = "at" + input_string[1:]

    # Step 6: Iterate through each character in the modified string
    for character in input_string:
        if character == "@":
            if count_at > 0:
                formatted_characters.append("at")
                count_at = 1
            else:
                formatted_characters.append("@")
                count_at = 1
        else:
            formatted_characters.append(character)

    # Step 7: Join the formatted characters into a single string
    output_string = ''.join(formatted_characters)

    # Step 8: Final formatting for the output string
    if output_string and output_string[-1] == ".":
        output_string = output_string[:-1] + "dot"

    # Step 9: Output the final formatted string
    print(output_string)

# In practice, the code can be tested by calling format_string()
# format_string()  # Uncomment to execute the function
