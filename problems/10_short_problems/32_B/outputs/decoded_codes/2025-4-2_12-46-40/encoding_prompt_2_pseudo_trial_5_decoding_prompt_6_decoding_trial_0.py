# Begin Program

# Read Input
input_string = input().strip()  # Accept user input and remove leading/trailing spaces

# Initialize Variables
index = 0  # Set index to 0 for tracking current position
output_string = ""  # Create an empty string to build the output

# Process Input
while index < len(input_string):  # Continue while index is less than the length of input_string
    if input_string[index] == '.':  # Check if the current character is a period
        output_string += '0'  # Append '0' to output_string
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check if the next character is a period
        output_string += '1'  # Append '1' to output_string
        index += 2  # Skip both characters
    else:
        output_string += '2'  # Append '2' to output_string
        index += 2  # Skip both characters

# Output Result
print(output_string)  # Print the final output_string

# End Program
