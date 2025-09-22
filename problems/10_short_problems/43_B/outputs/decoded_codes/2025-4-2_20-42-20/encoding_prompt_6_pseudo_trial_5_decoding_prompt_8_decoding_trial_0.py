# Step 1: Read two strings from user input
firstString = input()
secondString = input()

# Step 2: Remove spaces from both strings
firstString = firstString.replace(" ", "")
secondString = secondString.replace(" ", "")

# Step 3: Initialize a frequency list to store counts of character differences
characterFrequency = [0] * 128  # Assuming ASCII characters

# Step 4: Calculate the frequency of each character
for char in range(ord('A'), ord('z') + 1):
    countInFirstString = firstString.count(chr(char))
    countInSecondString = secondString.count(chr(char))
    
    # Calculate the difference in counts and store it in characterFrequency
    characterFrequency[char] = countInFirstString - countInSecondString

# Step 5: Check if all frequency differences are non-negative
isValid = True

for count in characterFrequency:
    if count < 0:
        isValid = False
        break  # No need to check further, exit loop

# Step 6: Output result based on validity check
if isValid:
    print("YES")
else:
    print("NO")
