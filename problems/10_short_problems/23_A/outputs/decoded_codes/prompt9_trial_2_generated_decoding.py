# Start of the program

# Step 2: Receive Input
input_string = input().strip()  # Read input and remove trailing newline
length_of_string = len(input_string)  # Store the length of the input string

# Step 3: Initialize a Variable
length_of_repeated_substring = 0  # Variable to track the longest repeated substring found

# Step 4: Search for Repeated Substrings
for l in range(1, length_of_string):  # Loop through possible lengths (1 to length_of_string)
    for i in range(length_of_string - l):  # Loop through starting indices for substring
        substring = input_string[i:i + l]  # Extract the substring of length `l`
        # Check if the substring appears again in the string starting from i + 1
        if substring in input_string[i + 1:]:
            length_of_repeated_substring = l  # Update the longest length found
            break  # Break out of inner loop as we only need one occurrence for this length

# Step 5: Output the Result
print(length_of_repeated_substring)  # Print the length of the longest repeated substring

# End of the program
