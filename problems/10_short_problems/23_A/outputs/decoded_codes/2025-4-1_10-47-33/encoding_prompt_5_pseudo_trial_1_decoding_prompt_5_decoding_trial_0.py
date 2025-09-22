# This program finds the length of the longest substring within a given string that occurs more than once

# Accept input from the user
input_string = input().strip()  # Read input and remove trailing whitespace
length_of_string = len(input_string)  # Determine the length of the input string

# Initialize a variable to keep track of the maximum length of repeating substrings
maximum_length = 0

# Loop through possible substring lengths
for substring_length in range(length_of_string):  # Starting from 0 up to n-1
    for start_index in range(length_of_string - substring_length):  # Start position for substring
        # Extract the substring of current length
        substring = input_string[start_index:start_index + substring_length + 1]
        
        # Check if the substring appears later in the input string
        if substring in input_string[start_index + 1:]:
            maximum_length = substring_length + 1  # Update maximum length
            break  # Exit inner loop to move to next substring length

# Output the maximum length of the repeating substring
print(maximum_length)
