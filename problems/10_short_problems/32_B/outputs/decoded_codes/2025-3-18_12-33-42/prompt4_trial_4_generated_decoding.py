# Begin the program

# Read input from standard input, removing any leading or trailing whitespace
input_string = input().strip()

# Initialize index i to 0
i = 0
# Initialize result_string as an empty string
result_string = ""

# Loop through the input string until the end is reached
while i < len(input_string):
    # Check the current character
    if input_string[i] == '.':
        result_string += '0'  # Append '0' to result_string
        i += 1  # Increment index i by 1
        
    elif (i + 1 < len(input_string)) and (input_string[i + 1] == '.'):
        result_string += '1'  # Append '1' to result_string
        i += 2  # Increment index i by 2
        
    else:
        result_string += '2'  # Append '2' to result_string
        i += 2  # Increment index i by 2

# Output the final result
print(result_string)

# End of program
