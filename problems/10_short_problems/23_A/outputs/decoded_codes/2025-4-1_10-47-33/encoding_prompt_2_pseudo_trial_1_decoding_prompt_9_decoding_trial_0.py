# Read input: Take a single line of input from the user
input_string = input().strip()

# Determine length: Calculate the length of the input string
string_length = len(input_string)

# Initialize variable: Set to zero (for tracking longest repeated substring length)
repeated_substring_length = 0

# Outer loop: For each possible substring length
for substring_length in range(1, string_length):  # Start from 1 to avoid empty substrings
    found_repeat = False  # Flag to track if a repeat is found

    # Inner loop: For each possible starting index
    for start_index in range(string_length - substring_length + 1):  
        # Extract the substring
        substring = input_string[start_index:start_index + substring_length]

        # Check if this substring appears again in the string after the current index
        if substring in input_string[start_index + substring_length:]:
            repeated_substring_length = substring_length  # Update the length
            found_repeat = True  # Set flag to true
            break  # Exit the inner loop if a repeat is found

    # Exit the outer loop if a repeat has been found
    if found_repeat:
        continue 

# Output result: Display the length of the longest repeated substring found
print(repeated_substring_length)
