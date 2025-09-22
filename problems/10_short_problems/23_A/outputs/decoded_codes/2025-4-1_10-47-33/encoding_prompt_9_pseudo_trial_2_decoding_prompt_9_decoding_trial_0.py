# Read Input
input_string = input()  # Obtain a string of characters from user input
string_length = len(input_string)  # Store the length of the string
longest_repeating_length = 0  # Initialize variable to hold the longest repeating substring length

# Iterate Through Substring Lengths
for current_length in range(1, string_length):  # current_length from 1 to string_length - 1
    for start_index in range(string_length - current_length):  # start index for substrings
        # Extract Substring
        substring = input_string[start_index:start_index + current_length]
        
        # Search for Repeats
        if substring in input_string[start_index + current_length:]:  # Check in the remaining part
            longest_repeating_length = current_length  # Update the longest repeating length found
            break  # Exit the inner loop as we found a repeat

# Output Result
print(longest_repeating_length)  # Print the length of the longest repeated substring found
