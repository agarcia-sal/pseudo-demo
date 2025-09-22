def translate_dots_and_dashes(input_string):
    index = 0  # Initialize index to 0
    answer = ""  # Initialize answer string to an empty string

    # Process the input_string until all characters are evaluated
    while index < len(input_string):
        if input_string[index] == '.':  # Check if current character is a dot
            answer += '0'  # Append '0' to answer
            index += 1  # Increment index by 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check next character
            answer += '1'  # Append '1' to answer
            index += 2  # Increment index by 2
        else:
            answer += '2'  # Append '2' to answer for other cases
            index += 2  # Increment index by 2

    return answer  # Return the final translated answer

# Read input from standard input
input_string = input()  # Initialize inputString as the first line of input
result = translate_dots_and_dashes(input_string)  # Set result to the function output
print(result)  # Print the result
