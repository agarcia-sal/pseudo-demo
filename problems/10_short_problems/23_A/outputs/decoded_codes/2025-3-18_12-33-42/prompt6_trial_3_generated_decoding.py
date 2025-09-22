# Read a single line of input
input_string = input()  # Read from standard input
string_length = len(input_string)  # Get the length of the input string
result_value = 0  # Initialize a variable to hold the result

# Loop over possible lengths of substrings (from 0 to length of the input string - 1)
for substring_length in range(string_length):  # Loop for substring lengths
    # Loop over the starting index of the substring
    for starting_index in range(string_length):  # Loop for starting index
        # Extract the substring from the input string
        substring = input_string[starting_index:starting_index + substring_length]

        # Check if this substring appears again in the string after its starting index
        if input_string.find(substring, starting_index + 1) != -1:
            result_value = substring_length  # Update the result with the current substring length
            break  # Exit the inner loop if a match is found

# Output the maximum length of the substring found that has duplicates
print(result_value)
