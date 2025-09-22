# Step 1: Import standard input functionality (no import needed for basic input)
# Step 2: Read a line of input from standard input and remove any trailing newline character
line = input().strip()

# Step 3: Set variable 'n' to the length of the input line
n = len(line)

# Step 4: Initialize variable 'rv' to 0; this will hold the result
rv = 0

# Step 5: Loop through each length 'l' from 0 to n-1
for l in range(n):
    # Step 6: Loop through each index 'i' from 0 to n-1
    for i in range(n):
        # Step 7: Extract the substring from 'line' starting at index 'i' with length 'l'
        substring = line[i:i + l]
        
        # Step 8: Check if this substring appears again in 'line' starting from index 'i + 1'
        if substring in line[i + 1:]:
            # Step 9: IF the substring is found THEN,
            # Step 10: Set 'rv' to the value of 'l'
            rv = l
            # Step 11: Break out of the inner loop
            break

# Step 12: Print the value of 'rv' (output the result)
print(rv)
