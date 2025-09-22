def translate_dots_and_dashes(input_string):
    index = 0                    # Initialize index to zero
    answer = ""                  # Initialize answer string as empty

    while index < len(input_string):  # Loop through the input string
        if input_string[index] == '.':  # Check if the current character is a dot
            answer += '0'          # Append '0' to answer
            index += 1             # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            answer += '1'          # Append '1' to answer
            index += 2             # Move past the two dots
        else:
            answer += '2'          # Append '2' for any other case (including a dash)
            index += 2             # Move past the two characters

    return answer                  # Return the final translated string


# Read input from standard input
input_string = input()           # Get the input string
result = translate_dots_and_dashes(input_string)  # Call the translation function
print(result)                   # Print the result
