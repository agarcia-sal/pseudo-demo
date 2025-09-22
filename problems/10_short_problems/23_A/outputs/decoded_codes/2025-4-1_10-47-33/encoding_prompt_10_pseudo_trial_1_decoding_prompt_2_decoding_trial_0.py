# Step 1: Read input and initialize variables
line = input().strip()  # Read a line of input from standard input
line = line[:-1]  # Remove the last character from line
n = len(line)  # Get the length of line
rv = 0  # This variable stores the result

# Step 2: Iterate through lengths l from 0 to n-1
for l in range(n):
    # Step 3: Check for substring presence
    for i in range(n):
        # Step 4: Check if the substring exists later in the string
        if line[i:i+l] in line[i+1:]:
            rv = l  # Update rv with the current length l
            break  # Exit the inner loop as the substring is found
    else:
        continue  # Continue with the outer loop if inner loop did not break
    break  # Break outer loop if inner loop was broken

# Step 5: Output the result
print(rv)  # Display the final value of rv
