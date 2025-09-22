# Start of the program

# Step 2: Receive Input
input_string = input()  # Read a line of text from the user
input_string = input_string.rstrip('\n')  # Remove the last character if it is a newline
length_of_string = len(input_string)  # Store the length of the string
longest_repeated_substring_length = 0  # Initialize the longest repeated substring length to zero

# Step 3: Loop Through Substring Lengths
for current_length in range(length_of_string):  # Loop through each possible length from 0 to length_of_string - 1
    for start_index in range(length_of_string):  # Loop through each starting index from 0 to length_of_string - 1
        # Extract the substring from start_index to start_index + current_length
        substring = input_string[start_index:start_index + current_length]  
        
        # Check if this substring occurs again in the string after start_index
        if substring and substring in input_string[start_index + 1:]:
            # If the substring is found, update the longest repeated substring length
            longest_repeated_substring_length = current_length 
            break  # Break out of the current loop as we only need the longest and first occurrence

# Step 4: Output Result
print(longest_repeated_substring_length)  # Print the length of the longest repeated substring

# End of the program
