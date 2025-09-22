# Step 1: Receive Input
input_line = input()  # Read a line of text from standard input
input_line = input_line[:-1]  # Remove the last character (newline)

# Step 2: Initialize Variables
length_of_line = len(input_line)  # Get the length of the input line
result_value = 0  # Initialize result value to 0

# Step 3: Loop through Possible Substring Lengths
for current_length in range(length_of_line):  # Loop from 0 to length_of_line - 1
    for current_index in range(length_of_line):  # Loop through each character position
        # Step 4: Check for Substring Reoccurrence
        substring = input_line[current_index:current_index + current_length]  # Define the substring
        if substring and input_line.find(substring, current_index + 1) != -1:  # Check if found again
            result_value = current_length  # Update result value to length of the substring
            break  # Exit the inner loop since we found a repeating substring

# Step 5: Output the Result
print(result_value)  # Output the value of result_value
