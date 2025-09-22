# BEGIN PROGRAM

# Read the input string from the user
input_string = input()  # Taking string input from user

# Initialize variables
index = 0  # Starting index for string traversal
output_string = ""  # String to store the output

# Loop through the input string until we reach the end
while index < len(input_string):  # Continue until the index reaches the end of the string
    if input_string[index] == '.':  # Check if the current character is '.'
        output_string += '0'  # If current character is a '.', append '0' to output_string
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check if next character is '.'
        output_string += '1'  # If next character is also '.', append '1' to output_string
        index += 2  # Move two characters ahead
    else:
        output_string += '2'  # Otherwise, append '2' to output_string
        index += 2  # Move two characters ahead

# Output the result
print(output_string)  # Printing the final output string

# END PROGRAM
