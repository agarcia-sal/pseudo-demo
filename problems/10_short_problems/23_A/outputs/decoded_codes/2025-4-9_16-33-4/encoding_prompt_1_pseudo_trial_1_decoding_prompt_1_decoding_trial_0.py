# START

# Read a line of input and remove the trailing newline character
inp = input()
inp_len = len(inp)
lon = 0

# Loop through all possible substring lengths
for sub in range(inp_len):  # sub goes from 0 to inp_len - 1
    # Check each starting position for the substring
    for star in range(inp_len):  # star goes from 0 to inp_len - 1
        # Extract the substring based on current length and starting position
        cur = inp[star:star + sub]  # Taking substring from star with length sub
        
        # Look for the occurrence of this substring starting after the current position
        if cur in inp[star + 1:]:  # Check if cur appears in inp starting from position star + 1
            # If found, update the longest repeated length
            lon = sub
            break  # using break out of the starting position loop

# Output the length of the longest repeating substring found
print(lon)

# END
