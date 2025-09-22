# Step 1: Read Input
input_string = input()
stringLength = len(input_string)
longestRepeatingSubstringLength = 0

# Step 2: Iterate Through Substring Lengths
for currentLength in range(1, stringLength):  # Start from 1 to avoid empty substring
    for startIndex in range(stringLength - currentLength + 1):
        
        # Step 2.1: Extract Substring
        substring = input_string[startIndex:startIndex + currentLength]
        
        # Step 2.2: Search for Repeats
        if substring in input_string[startIndex + currentLength:]:
            longestRepeatingSubstringLength = currentLength
            break  # Exit the inner loop because we found a repeat

# Step 3: Output Result
print(longestRepeatingSubstringLength)
