def transform_string():
    # Step 1: Read input and initialize variables
    input_string = input().strip()  # Read input and remove leading/trailing spaces
    index = 0
    answer = ""

    # Step 2: Process each character in the input string
    while index < len(input_string):
        if input_string[index] == '.':
            answer += '0'  # Append '0' if current character is '.'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            answer += '1'  # Append '1' if the next character is '.'
            index += 2
        else:
            answer += '2'  # Append '2' for all other cases
            index += 2

    # Step 3: Output the result
    print(answer)

# Example of how to call the function
if __name__ == "__main__":
    transform_string()
