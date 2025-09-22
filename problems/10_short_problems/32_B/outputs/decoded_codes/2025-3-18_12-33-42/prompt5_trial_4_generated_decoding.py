# Initialize an empty string to store the user input
input_string = input().strip()

# Initialize index to keep track of the current position in the string
index = 0

# Initialize an empty string to concatenate the results
result_string = ""

# Process the input string while index is less than its length
while index < len(input_string):
    # Check if the current character is a dot
    if input_string[index] == '.':
        result_string += '0'  # Append '0' for a single dot
        index += 1  # Move to the next character
    # Check if the next character is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result_string += '1'  # Append '1' for two consecutive dots
        index += 2  # Skip both current and next character
    else:
        result_string += '2'  # Append '2' for any other character pair
        index += 2  # Skip both current and next character

# Print the final result string
print(result_string)

# Example test cases (uncomment to test):
# Input: ".." -> Output: "00"
# Input: ".-" -> Output: "01"
# Input: "--" -> Output: "2"
