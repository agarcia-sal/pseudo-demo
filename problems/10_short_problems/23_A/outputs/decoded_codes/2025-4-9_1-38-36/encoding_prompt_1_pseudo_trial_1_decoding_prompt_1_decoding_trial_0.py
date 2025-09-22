# 1. Start the program

# 2. Read input string from user
input_string = input().rstrip('\n')  # Remove newline character if any

# 3. Initialize variables
total_length = len(input_string)
longest_repeated_length = 0  # This will store the length of the longest repeating substring

# 4. Loop over possible substring lengths
for current_length in range(total_length):  # From 0 to total_length - 1
    # Nested Loop over starting positions of substrings
    for start_index in range(total_length):  # From 0 to total_length - 1
        substring = input_string[start_index:start_index + current_length]  # Extract the substring
        # Check if this substring appears again in the string
        if substring in input_string[start_index + 1:]:  # Check for repetition
            longest_repeated_length = current_length  # Update the length of the longest repeating substring
            break  # Exit the loop as we found a repeating substring of this length

# 5. Output the result
print(longest_repeated_length)  # Print the length of the longest substring that appears more than once

# 6. End the program
