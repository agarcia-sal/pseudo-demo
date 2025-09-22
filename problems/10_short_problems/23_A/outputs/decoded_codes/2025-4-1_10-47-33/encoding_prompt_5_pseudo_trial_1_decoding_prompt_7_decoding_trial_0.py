# Purpose: To find the length of the longest substring within a given string that occurs more than once.

# Step 1: Accept Input
line = input().strip()  # Read a line of text from the user and remove any trailing newline/whitespace.
n = len(line)  # Determine the length of the input string.

# Step 2: Initialize Variables
maximum_length = 0  # This variable keeps track of the maximum length of the repeating substring found.

# Step 3: Loop Through Possible Substring Lengths
for l in range(1, n):  # We start from length 1 since a length of 0 does not make sense for substrings.
    # Step 4: Inner Loop to Check Substrings
    for i in range(n - l + 1):  # Loop from 0 to n - l to get valid starting positions for the substring.
        substring = line[i:i + l]  # Extract the substring starting at position i of length l.

        # Step 5: Search for this substring within the rest of the input string
        if substring in line[i + 1:]:  # Check if the substring can be found later in the string.
            maximum_length = l  # Update maximum_length to the current length.
            break  # Exit the inner loop, move to the next length 'l'.

# Step 6: Output Result
print(maximum_length)  # Print the maximum length of the repeating substring that is found.
