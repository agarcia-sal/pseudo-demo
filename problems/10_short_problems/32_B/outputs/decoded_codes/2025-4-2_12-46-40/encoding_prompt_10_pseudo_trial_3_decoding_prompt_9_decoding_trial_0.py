# Step 1: Read input and initialize variables
input_string = input().strip()  # Read input and remove trailing spaces
index = 0
answer = ""  # Initialize the answer as an empty string

# Step 2: Process each character in the input string
while index < len(input_string):
    if input_string[index] == '.':
        answer += '0'  # Append '0' if current character is '.'
        index += 1
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        answer += '1'  # Append '1' if the next character is '.' 
        index += 2  # Increment index by 2 since we processed two characters
    else:
        answer += '2'  # Append '2' for any other cases
        index += 2  # Increment by 2 as well

# Step 3: Output the result
print(answer)
