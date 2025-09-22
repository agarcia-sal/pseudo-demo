line = input().strip()  # Read a line of input and remove the newline
line_length = len(line)  # Get the length of the input line
result_value = 0  # Initialize result to hold the maximum length of found repeated substring

# Loop through all possible substring lengths from 0 to line_length - 1
for l in range(line_length):  # 'l' represents the length of the substring
    # Loop through each index in the line to check for repeated substrings
    for i in range(line_length):  # 'i' is the starting index of the substring
        # Extract a substring of length l starting from current index i
        substring = line[i:i + l]  # Extract the substring from index i for length l
        
        # Check if this substring occurs again later in the line
        if line.find(substring, i + 1) != -1:  # Using find to check for occurrence after index i
            result_value = l  # Update the result_value to the current length l
            break  # Break out of the inner loop if a repeated substring is found

# Output the maximum length of the found repeated substring
print(result_value)
