# Step 1: Read two strings from user input
firstString = input()
secondString = input()

# Step 2: Remove spaces from both strings
firstString = firstString.replace(" ", "")
secondString = secondString.replace(" ", "")

# Step 3: Initialize a frequency list to store counts of character differences
# ASCII characters range from 0 to 127, so we need a list of size 128
characterFrequency = [0] * 128

# Step 4: Calculate the frequency of each character
for character in range(ord('A'), ord('z') + 1):  # Loop from ASCII 'A' to 'z'
    countInFirstString = firstString.count(chr(character))
    countInSecondString = secondString.count(chr(character))
    
    # Calculate the difference in counts and store it in characterFrequency
    characterFrequency[character] = countInFirstString - countInSecondString

# Step 5: Check if all frequency differences are non-negative
isValid = True  # Default value is TRUE

for count in characterFrequency:
    if count < 0:
        isValid = False
        break  # No need to check further, exit loop

# Step 6: Output result based on validity check
if isValid:
    print("YES")
else:
    print("NO")
