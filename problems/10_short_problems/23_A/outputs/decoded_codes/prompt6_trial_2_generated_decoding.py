# Step 1: Read a line of input from standard input
input_line = input()

# Step 2: Determine the length of the input line
length_of_input = len(input_line)

# Step 3: Initialize the variable to keep track of the longest repeated substring length
longest_repeated_length = 0

# Step 4: Iterate through all possible substring lengths from 0 to length_of_input - 1
for substring_length in range(length_of_input):
    
    # Step 5: Check all starting positions for the current substring length
    for starting_index in range(length_of_input):
        
        # Step 6: Extract the substring from the current starting index with the current length
        substring = input_line[starting_index:starting_index + substring_length + 1]
        
        # Step 7: Check if this substring appears again in input_line after the current position
        if substring in input_line[starting_index + 1:]:
            longest_repeated_length = substring_length
            break  # Break out of the inner loop if a repeated substring is found

# Step 8: Output the length of the longest repeated substring found
print(longest_repeated_length)
