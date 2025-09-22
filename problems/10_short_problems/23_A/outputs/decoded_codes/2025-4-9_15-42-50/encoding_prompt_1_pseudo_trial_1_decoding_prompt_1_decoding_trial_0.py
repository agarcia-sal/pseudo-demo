# Start of the program

# Read a line of input and remove the trailing newline character
inp = input()
inp_len = len(inp)
lon = 0

# Loop through all possible substring lengths
for sub in range(inp_len):
    # Check each starting position for the substring
    for star in range(inp_len):
        # Extract the substring based on current length and starting position
        cur = inp[star:star + sub]
        
        # Look for the occurrence of this substring starting after the current position
        if cur in inp[star + 1:]:
            # If found, update the longest repeated length
            lon = sub
            break  # out of the starting position loop

# Output the length of the longest repeating substring found
print(lon)

# End of the program
