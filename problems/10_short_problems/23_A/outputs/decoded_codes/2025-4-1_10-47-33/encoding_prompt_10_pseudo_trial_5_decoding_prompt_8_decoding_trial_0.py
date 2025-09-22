# Step 1: Importing standard input functionality
import sys

# Step 2: Reading a line of input from standard input and removing the trailing newline character
line = sys.stdin.readline().strip()

# Step 3: Setting variable 'n' to the length of the input line
n = len(line)

# Step 4: Initializing variable 'rv' to 0
rv = 0

# Step 5: FOR each length 'l' from 0 to n-1
for l in range(n):
    # Step 6: FOR each index 'i' from 0 to n-1
    for i in range(n):
        # Step 7: Extracting the substring from 'line'
        substring = line[i:i+l]
        
        # Step 8: Checking if the substring appears again in 'line' starting from index 'i + 1'
        if substring in line[i + 1:]:
            # Step 9: IF the substring is found
            rv = l  # Step 10: Set 'rv' to the value of 'l'
            break  # Step 11: Break out of the inner loop

# Step 12: Print the value of 'rv'
print(rv)
