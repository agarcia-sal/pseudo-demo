# Function to transform the input string based on specific character rules
def transform_string():
    # Step 1: Read input and initialize variables
    input_string = input().strip()  # Read a line from standard input and remove trailing spaces
    index = 0
    answer = ""

    # Step 2: Process each character in the input string
    while index < len(input_string):
        if input_string[index] == '.':
            answer += '0'  # Append '0' if the current character is '.'
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            answer += '1'  # Append '1' if the next character is '.'
            index += 2  # Skipping both characters
        else:
            answer += '2'  # Append '2' for any other character
            index += 2  # Skipping the current character

    # Step 3: Output the result
    print(answer)

# Run the function
transform_string()
