# Step 1: Read input
input_string = input().rstrip()

# Step 2: Determine length
stringLength = len(input_string)

# Step 3: Initialize variable
repeatedSubstringLength = 0

# Step 4: Outer loop for each possible substring length
for substringLength in range(1, stringLength):  # substringLength from 1 to stringLength - 1
    # Step 4.1: Inner loop for each possible starting index
    for startIndex in range(stringLength - substringLength + 1):  # Ensure we stay within bounds
        # Step 4.2: Extract the substring
        substring = input_string[startIndex:startIndex + substringLength]
        
        # Step 4.3: Check if the substring appears again after the current index
        if input_string.find(substring, startIndex + 1) != -1:
            # Step 4.4: Update repeatedSubstringLength and exit inner loop
            repeatedSubstringLength = substringLength
            break  # Exit inner loop

# Step 5: Output result
print(repeatedSubstringLength)
