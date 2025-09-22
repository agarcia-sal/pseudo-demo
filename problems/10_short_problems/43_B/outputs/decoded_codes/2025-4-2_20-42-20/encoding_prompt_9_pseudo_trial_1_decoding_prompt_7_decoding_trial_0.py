# Step 1: Retrieve Input
# Get the first string from the user
firstString = input()
# Get the second string from the user
secondString = input()

# Step 2: Preprocess Input
# Create a cleaned version of the strings by removing spaces
cleanedStrings = [
    firstString.replace(" ", ""),
    secondString.replace(" ", "")
]
s1 = cleanedStrings[0]  # Assign cleaned first string
s2 = cleanedStrings[1]  # Assign cleaned second string

# Step 3: Count Character Frequencies
# Initialize a list to store the frequency difference
frequencyDifference = []

# ASCII range for uppercase 'A' to lowercase 'z'
for char in range(ord('A'), ord('z') + 1):
    # Count how many times this character appears in s1
    count_s1 = s1.count(chr(char))
    # Count how many times this character appears in s2
    count_s2 = s2.count(chr(char))
    # Calculate the difference and append to the list
    frequencyDifference.append(count_s1 - count_s2)

# Step 4: Check Character Count Requirements
# Count how many values in frequencyDifference are less than zero
insufficientCount = sum(1 for diff in frequencyDifference if diff < 0)

# Step 5: Provide Output
if insufficientCount == 0:
    print("YES")  # Transformation is possible
else:
    print("NO")   # Transformation is not possible
