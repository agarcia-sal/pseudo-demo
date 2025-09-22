# Start of the program

# Step 1: Read two strings from user input
firstString = input()
secondString = input()

# Step 2: Remove spaces from both strings
firstString = firstString.replace(" ", "")
secondString = secondString.replace(" ", "")

# Step 3: Initialize a frequency list to store counts of character differences
# The size is based on the ASCII values of characters, assuming a size of 128 to cover all standard ASCII characters
characterFrequency = [0] * 128

# Step 4: Calculate the frequency of each character
for character in range(65, 123):  # ASCII range for 'A' (65) to 'z' (122)
    char = chr(character)  # Convert ASCII code to character
    
    # Count occurrences of the character in both strings
    countInFirstString = firstString.count(char)
    countInSecondString = secondString.count(char)
    
    # Calculate the difference in counts and store it in characterFrequency
    characterFrequency[character] = countInFirstString - countInSecondString

# Step 5: Check if all frequency differences are non-negative
isValid = True  # Default assumption is that the frequencies are valid

for count in characterFrequency:
    if count < 0:
        isValid = False
        break  # No need to check further, exit loop

# Step 6: Output result based on validity check
if isValid:
    print("YES")
else:
    print("NO")

# End of the program
