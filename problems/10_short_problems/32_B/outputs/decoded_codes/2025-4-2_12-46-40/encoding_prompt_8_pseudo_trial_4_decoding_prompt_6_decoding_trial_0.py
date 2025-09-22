# Step 1: Read input
input_string = input().strip()  # Get a line of input and remove extra spaces or newline characters

# Step 2: Initialize variables
current_position = 0  # Index to track position in input string
result = ""  # Empty string to store the translated numerical output

# Step 3: Process the input
while current_position < len(input_string):  # Continue until we reach the end of the input string
    if input_string[current_position] == '.':  # Check for a single dot
        result += '0'  # Add '0' to result
        current_position += 1  # Move one step forward
    else:  # If the current character is not a dot
        if current_position + 1 < len(input_string) and input_string[current_position + 1] == '.':  # Check next character
            result += '1'  # Add '1' to result for two dots
            current_position += 2  # Move two steps forward
        else:  # If the next character is neither a dot nor we are at the end
            result += '2'  # Add '2' to result
            current_position += 2  # Move two steps forward

# Step 4: Output the result
print(result)  # Printing the final translated numerical output
