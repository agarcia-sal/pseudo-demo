# Begin the program

# Read input string from the user
input_string = input()

# Remove whitespace from both ends of the input string
input_string = input_string.strip()

# Initialize index counter
index = 0

# Initialize the answer string to empty
answer_string = ""

# Loop until index reaches the length of the input string
while index < len(input_string):
    # Check if the current character is a dot
    if input_string[index] == '.':
        # Append '0' to the answer string
        answer_string += '0'
        # Move to the next character
        index += 1
    # Check if the next character is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        # Append '1' to the answer string
        answer_string += '1'
        # Move to the character after next
        index += 2
    else:
        # Append '2' to the answer string
        answer_string += '2'
        # Move to the character after next
        index += 2

# Output the final answer string
print(answer_string)

# End of the program
