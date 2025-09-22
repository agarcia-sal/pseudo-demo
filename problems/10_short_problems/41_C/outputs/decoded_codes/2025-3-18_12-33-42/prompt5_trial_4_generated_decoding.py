# Function to format a given string input according to specified rules
def format_string():
    # 1. Read Input and remove whitespace
    input_string = input().strip()
    
    # 2. Replace "dot" with "." and "at" with "@"
    input_string = input_string.replace("dot", ".").replace("at", "@")
    
    # 3. Fix starting character - prepend "dot" if input starts with "."
    if input_string.startswith("."):
        input_string = "dot" + input_string
    
    # 4. Initialize variables
    consecutive_at_count = 0  # Counter for "@"
    formatted_chars = []  # List to hold the formatted characters
    
    # 5. Ensure valid "at" format - prepend "at" if input starts with "@"
    if input_string.startswith("@"):
        input_string = "at" + input_string

    # 6. Construct final output by processing characters
    for character in input_string:
        if character == "@":
            if consecutive_at_count > 0:
                formatted_chars.append("at")  # Append "at" if "@" encountered again
            else:
                formatted_chars.append("@")  # First encounter of "@"
            consecutive_at_count += 1
        else:
            formatted_chars.append(character)  # Append other characters

    # 7. Handle trailing period
    if formatted_chars and formatted_chars[-1] == ".":
        formatted_chars.pop()  # Remove last character which is "."
        formatted_chars.append("dot")  # Append "dot"

    # 8. Output the result
    final_string = ''.join(formatted_chars)  # Join characters to form final string
    print(final_string)  # Print the formatted string

# Example execution
format_string()
