# Read a line from standard input and remove the trailing newline character
line = input().strip()
n = len(line)
rv = 0  # Initialize the result variable

# Loop through all possible lengths of substrings
for l in range(n):  # l goes from 0 to n-1
    # Loop through each starting position in the line
    for i in range(n):  # i goes from 0 to n-1
        # Check if the substring from position i of length l appears again in the line after position i
        substring = line[i:i + l]
        if substring and line.find(substring, i + 1) != -1:
            # Update the result with the current length l
            rv = l
            break  # Exit the inner loop since we found a valid substring
    else:
        continue  # Continue with the next length l if inner loop didn't break

# Output the result
print(rv)
