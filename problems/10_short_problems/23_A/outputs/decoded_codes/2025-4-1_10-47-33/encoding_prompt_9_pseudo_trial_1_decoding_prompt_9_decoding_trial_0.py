# Read the input string from standard input, stripping off the last character
input_string = input()[:-1]
length_of_string = len(input_string)
longest_repeated_length = 0

# Iterate through possible substring lengths
for substring_length in range(length_of_string):
    for index in range(length_of_string):
        # Extract the current substring from input_string
        current_substring = input_string[index:index + substring_length]

        # Check if current_substring appears again in input_string starting from index + 1
        if current_substring in input_string[index + 1:]:
            longest_repeated_length = substring_length

            # Exit the inner loop as we found a repeated substring of this length
            break

# Output the length of the longest repeated substring
print(longest_repeated_length)
