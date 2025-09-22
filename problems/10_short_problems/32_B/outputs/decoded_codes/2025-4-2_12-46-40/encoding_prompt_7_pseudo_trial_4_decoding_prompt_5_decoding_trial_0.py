def translate_dots_and_dashes(input_string):
    index = 0               # Initialize index to 0
    answer = ""             # Initialize an empty string for the answer

    while index < len(input_string):  # Loop through the input string
        # Check conditions based on the characters in the input string
        if input_string[index] == '.':
            answer += '0'   # Append '0' for a single dot
            index += 1      # Increment index by 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            answer += '1'   # Append '1' for a dot followed by a dot
            index += 2      # Increment index by 2
        else:
            answer += '2'   # Append '2' for all other combinations
            index += 2      # Increment index by 2

    return answer           # Return the final answer


# Read input from standard input
input_string = input()
result = translate_dots_and_dashes(input_string)
print(result)  # Output the result
