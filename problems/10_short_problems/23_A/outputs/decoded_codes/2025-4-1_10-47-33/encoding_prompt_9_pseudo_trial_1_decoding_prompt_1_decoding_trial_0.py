# START

input_string = input()[:-1]  # Read the input and remove the last character
length_of_string = len(input_string)
longest_repeated_length = 0

for substring_length in range(length_of_string):  # Loop over substring lengths
    for index in range(length_of_string):  # Loop over starting indices
        current_substring = input_string[index:index + substring_length]  # Get the current substring

        # Check if current_substring appears again in input_string starting from index + 1
        if input_string.find(current_substring, index + 1) != -1:
            longest_repeated_length = substring_length  # Update longest repeated length
            break  # Exit the inner loop

# OUTPUT
print(longest_repeated_length)

# END
