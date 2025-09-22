# Function to read input from standard input
input_string = input()  # Read the input string

# Get the length of the input string
string_length = len(input_string)

# Initialize a variable to store the length of the longest prefix found
longest_prefix_length = 0

# Loop through all potential prefix lengths
for current_length in range(string_length):  # current_length from 0 to string_length - 1

    # Check each starting position for the prefix in the input string
    for start_position in range(string_length):  # startPosition from 0 to string_length - 1
        
        # Extract the substring for the current prefix length starting from start_position
        substring = input_string[start_position:start_position + current_length]

        # If the substring exists again in the string after the starting position
        if input_string.find(substring, start_position + 1) != -1:
            longest_prefix_length = current_length  # Update longest prefix length
            break  # Exit the inner loop if a match is found

# Output the length of the longest prefix found
print(longest_prefix_length)
