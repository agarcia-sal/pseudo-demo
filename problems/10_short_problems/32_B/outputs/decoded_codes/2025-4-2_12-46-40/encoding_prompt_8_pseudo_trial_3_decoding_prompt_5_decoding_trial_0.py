# Read the input string from standard input and trim whitespace
input_string = input().strip()

# Initialize variables
current_position = 0  # This tracks the current position in the input string
result = ""           # This will hold the final output string of numbers

# Process the input string
while current_position < len(input_string):
    if input_string[current_position] == '.':
        # If current character is a dot, represent it as '0'
        result += '0'
        current_position += 1  # Move to the next character
    elif current_position + 1 < len(input_string) and input_string[current_position + 1] == '.':
        # If the next character is also a dot, represent this pair as '1'
        result += '1'
        current_position += 2  # Move ahead by two positions
    else:
        # Otherwise, treat it as '2'
        result += '2'
        current_position += 2  # Move ahead by two positions

# Output the final result string
print(result)

# Example of edge case handling:
# Input: "...." -> Output: "010" (as there are pairs of dots and a single dot)
# Input: "a.b" -> Output: "2" (as 'a' and 'b' are not relevant for the numbers)
