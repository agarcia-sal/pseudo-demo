def process_string(input_string):
    # Remove any surrounding whitespace from the input string
    s = input_string.strip()

    # Initialize the index and the answer variable
    index = 0
    answer = ''

    # Loop through characters in the string until the end is reached
    while index < len(s):
        if s[index] == '.':
            # If it's a single dot, append '0' to the answer
            answer += '0'
            index += 1
        elif index + 1 < len(s) and s[index + 1] == '.':
            # If the next character is a dot, append '1' to the answer
            answer += '1'
            index += 2
        else:
            # In all other cases, append '2' to the answer
            answer += '2'
            index += 2

    return answer

if __name__ == "__main__":
    # Read a line of input
    user_input = input()
    # Process the input and print the output
    result = process_string(user_input)
    print(result)
