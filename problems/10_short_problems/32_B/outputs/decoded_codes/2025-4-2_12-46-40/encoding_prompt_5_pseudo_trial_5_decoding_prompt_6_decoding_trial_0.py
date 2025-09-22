# Receive input
input_string = input().strip()  # Read input and remove surrounding spaces

# Initialize variables
index = 0  # To track the current position in the input string
output_string = ""  # To store the decoded result

# Process input string
while index < len(input_string):  # Continue until we process the entire string
    if input_string[index] == '.':  # Check if the current character is a dot
        output_string += '0'  # Append '0' to output_string
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check the next character is also a dot
        output_string += '1'  # Append '1' to output_string
        index += 2  # Move past this pair of characters
    else:  # If neither of the above conditions are met
        output_string += '2'  # Append '2' to output_string
        index += 2  # Move past this pair of characters

# Output the result
print(output_string)  # Print the decoded output string
