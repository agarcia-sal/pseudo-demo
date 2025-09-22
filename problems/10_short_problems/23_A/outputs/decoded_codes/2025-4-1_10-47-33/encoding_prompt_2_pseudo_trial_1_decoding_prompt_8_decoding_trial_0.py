# Step 1: Read input
input_string = input().strip()

# Step 2: Determine length
stringLength = len(input_string)

# Step 3: Initialize variable
repeatedSubstringLength = 0

# Step 4: Outer loop for each possible substring length
for substringLength in range(1, stringLength):  # start from 1 to avoid empty substring
    # Step 4.1: Inner loop for each possible starting index
    for startIndex in range(stringLength - substringLength + 1):
        # Extract the substring
        substring = input_string[startIndex:startIndex + substringLength]
        
        # Check if the substring appears again in the string after the current index
        if input_string.find(substring, startIndex + 1) != -1:
            repeatedSubstringLength = substringLength
            break  # Exit inner loop once a repeat is found

# Step 5: Output result
print(repeatedSubstringLength)
