# Read a line of input
input_line = input().strip()  # Removing any trailing newlines or spaces
length_of_input = len(input_line)
longest_repeated_length = 0

# Loop through all possible substring lengths from 1 to (length of input)
for substring_length in range(1, length_of_input):
    found_repeat = False  # Variable to track if a repeat has been found for the current length

    # Loop through all starting positions of the substring in the input
    for start_index in range(length_of_input - substring_length + 1):
        # Extract the current substring based on the start_index and substring_length
        current_substring = input_line[start_index:start_index + substring_length]
        
        # Check if the current substring appears again in the input beyond its starting position
        if current_substring in input_line[start_index + 1:]:
            longest_repeated_length = substring_length  # Update the length of the longest repeated substring found
            found_repeat = True  # A repeat was found, exit the inner loop
            break  # Exit the inner loop as we already found a repeat for this substring length
    
    if found_repeat:  # No need to check longer lengths if we found a repeat for this length
        continue

# Output the length of the longest repeated substring
print(longest_repeated_length)
