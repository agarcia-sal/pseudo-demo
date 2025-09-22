# Step 1: Importing the necessary functionality
# (Not needed since standard input is already available in Python)

# Step 2: Read a line of input and strip any trailing newline characters
line = input().rstrip()

# Step 3: Set variable 'n' to the length of the input line
n = len(line)

# Step 4: Initialize variable 'rv' which will hold the result
rv = 0

# Step 5: Iterate over each length 'l' from 0 to n-1
for l in range(n):
    # Step 6: Iterate over each index 'i' from 0 to n-1
    for i in range(n):
        # Step 7: Check if we can extract a substring of length 'l' starting from index 'i'
        substring = line[i:i + l]
        
        # Ensure we don't go beyond the string's bounds
        if len(substring) == l and substring in line[i + 1:]:
            # Step 9: If the substring is found starting from index 'i + 1'
            rv = l  # Step 10: Set 'rv' to the value of 'l'
            break  # Step 11: We found a match, exit the loop for indices 'i'

# Step 12: Print the value of 'rv', the result of our search
print(rv)
