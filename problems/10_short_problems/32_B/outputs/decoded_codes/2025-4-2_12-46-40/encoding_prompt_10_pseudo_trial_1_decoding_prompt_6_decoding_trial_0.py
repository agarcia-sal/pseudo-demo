# Begin the program

# Read input string from standard input
input_string = input()

# Initialize index variable
index = 0

# Initialize answer as an empty string
answer = ""

# Loop through each character of the string
while index < len(input_string):
    # Check if the current character is a dot
    if input_string[index] == '.':
        # Append '0' to the answer
        answer += '0'
        # Move to the next character
        index += 1
    else:
        # Check the next character for a dot
        if index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' to the answer
            answer += '1'
            # Move past both characters
            index += 2
        else:
            # Append '2' to the answer
            answer += '2'
            # Move past both characters
            index += 2

# Output the final result
print(answer)

# End of program
