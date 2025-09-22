# Step 1: Read a line of input and remove the trailing newline character
inp = input().strip()  # Using .strip() to remove newline and any extra spaces

# Step 2: Determine the length of the input string
inp_len = len(inp)  # Using len() to get the length of the string

# Step 3: Initialize a variable to store the length of the longest repeating substring
lon = 0

# Step 4: Iterate through possible lengths of substrings starting from 0 up to the length of the input
for sub in range(inp_len):
    # Check every starting index in the string for the given substring length
    for star in range(inp_len):
        # Extract the current substring from the input string
        cur = inp[star:star + sub]  # Python string slicing to get the substring
        
        # If the substring is found again starting from the next index
        if cur and inp.find(cur, star + 1) != -1:  # Check if cur is not empty and find returns an index
            # Update the longest repeating length if a longer substring is found
            lon = sub
            break  # Exit the inner loop and check the next substring length

# Step 5: Output the length of the longest repeating substring
print(lon)  # Using print() to display the final value
