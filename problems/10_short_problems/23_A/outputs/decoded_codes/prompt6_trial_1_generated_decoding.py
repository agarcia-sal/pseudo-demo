# Begin the program

# Read a line of input from the user
input_string = input()

# Determine the length of the input string
string_length = len(input_string)

# Initialize a variable to hold the result for the maximum repeated length
maximum_repeated_length = 0

# Loop over all possible lengths of substrings
for current_length in range(1, string_length):  # Start from 1, as length 0 is not useful
    # Loop through each position in the string
    for index in range(string_length):
        # Extract the substring from the current index with the current length
        substring = input_string[index:index + current_length]
        
        # Check if this substring appears again in the input_string after the current index position
        if input_string.find(substring, index + 1) != -1:
            # Update the maximum repeated length found
            maximum_repeated_length = current_length
            # Exit the inner loop since we found a repeated substring
            break 

# Output the maximum length of repeated substrings found
print(maximum_repeated_length)
