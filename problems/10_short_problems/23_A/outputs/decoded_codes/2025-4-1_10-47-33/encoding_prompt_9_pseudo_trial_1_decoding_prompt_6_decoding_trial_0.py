# Begin by reading the input string and removing the last character
input_string = input()[:-1]
# Calculate the length of the input string
length_of_string = len(input_string)
# Initialize the length of the longest repeated substring to zero
longest_repeated_length = 0

# Iterate over possible substring lengths
for substring_length in range(1, length_of_string):  # start from 1 to avoid empty substring
    # Iterate over each index to extract substrings
    for index in range(length_of_string - substring_length + 1):
        # Define the current substring based on the current index and length
        current_substring = input_string[index:index + substring_length]
        
        # Check if the current substring appears again in the string from the next index
        if current_substring in input_string[index + 1:]:
            # Update the longest repeated substring length if found
            longest_repeated_length = substring_length
            
            # Exit the inner loop since we found a repeated substring
            break

# Output the length of the longest repeated substring
print(longest_repeated_length)
