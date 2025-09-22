# Step 1: Read a line of input from standard input
line = input().strip()  # Read input and remove any trailing newline characters

# Step 2: Set variable 'n' to the length of the input line
n = len(line)

# Step 3: Initialize variable 'rv' to 0 to hold the result
rv = 0

# Step 4: Iterate over possible lengths 'l' of substrings from 1 to n-1
for l in range(1, n):  # Starts from 1 because an empty substring is not valid
    # Step 5: Iterate over each starting index 'i' for the substring
    for i in range(n - l + 1):  # Ensures we don't go out of bounds
        # Step 6: Extract the substring
        substring = line[i:i+l]  # Extract substring starting from index 'i' with length 'l'
        
        # Step 7: Check if this substring appears again in 'line' starting from 'i + 1'
        if substring in line[i+1:]:  # Check remaining part of the string for the substring
            rv = l  # Update the result with the length of the substring
            break  # Exit the inner loop since we found a match

# Step 8: Print the value of 'rv'
print(rv)  # Output the result
