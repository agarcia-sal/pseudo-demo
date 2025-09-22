# Step 1: Read input
input_string = input().strip()

# Step 2: Determine length
stringLength = len(input_string)

# Step 3: Initialize variable
repeatedSubstringLength = 0

# Step 4: Outer loop
for substringLength in range(stringLength):
    # Step 4.1: Inner loop
    for index in range(stringLength):
        # Step 4.2: Extract substring
        substring = input_string[index:index + substringLength]

        # Step 4.3: Check if the substring appears again
        if substring in input_string[index + 1:]:
            # Step 4.4: Update repeatedSubstringLength
            repeatedSubstringLength = substringLength
            break  # Exit inner loop upon finding a repeat

# Step 5: Output result
print(repeatedSubstringLength)
