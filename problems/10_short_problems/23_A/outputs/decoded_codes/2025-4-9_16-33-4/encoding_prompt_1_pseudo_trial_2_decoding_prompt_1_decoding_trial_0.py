# Read a line of input and remove the trailing newline character
inp = input().strip()

# Determine the length of the input string
inp_len = len(inp)

# Initialize a variable to store the length of the longest repeating substring
lon = 0

# Iterate through possible lengths of substrings starting from 0 up to the length of the input
for sub in range(inp_len):
    # Check every starting index in the string for the given substring length
    for star in range(inp_len):
        # Extract the current substring from the input string
        cur = inp[star:star + sub]

        # If the substring is found again starting from the next index
        if inp.find(cur, star + 1) != -1:
            # Update the longest repeating length if a longer substring is found
            lon = sub
            break  # Exit the inner loop and check the next substring length

# Output the length of the longest repeating substring
print(lon)
