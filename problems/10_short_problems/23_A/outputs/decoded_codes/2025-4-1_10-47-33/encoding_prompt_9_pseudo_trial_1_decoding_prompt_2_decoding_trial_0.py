# START

# Read input string and remove the last character
input_string = input()[:-1]
length_of_string = len(input_string)
longest_repeated_length = 0

# Outer loop: iterate over possible substring lengths
for substring_length in range(length_of_string):
    # Inner loop: iterate over each starting index for the substring
    for index in range(length_of_string):
        # Define the current substring
        current_substring = input_string[index:index + substring_length]

        # Check if the current_substring appears again in input_string starting from index + 1
        if input_string.find(current_substring, index + 1) != -1:
            longest_repeated_length = substring_length

            # Exit the inner loop as we found a repeated substring of this length
            break
    # No need for an additional break here; it will naturally proceed to the next substring_length

# OUTPUT
print(longest_repeated_length)

# END
