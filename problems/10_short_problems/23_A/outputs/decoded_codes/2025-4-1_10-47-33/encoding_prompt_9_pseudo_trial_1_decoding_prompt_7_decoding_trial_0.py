# Start of the program

# Read input string from standard input and remove the last character
input_string = input()[:-1]

# Calculate the length of the input string
length_of_string = len(input_string)

# Initialize the variable to track the length of the longest repeated substring
longest_repeated_length = 0

# Outer loop: iterate over possible lengths of substrings
for substring_length in range(1, length_of_string):  # Start from 1 to avoid empty substring
    # Inner loop: iterate over possible starting indices for the substring
    for index in range(length_of_string - substring_length + 1):
        # Define the current substring from input_string
        current_substring = input_string[index:index + substring_length]

        # Check if current_substring appears again in input_string starting from index + 1
        if current_substring in input_string[index + 1:]:
            # Found a repeated substring
            longest_repeated_length = substring_length
            # Exit the inner loop as we found a repeated substring of this length
            break

# Output the length of the longest repeating substring
print(longest_repeated_length)
