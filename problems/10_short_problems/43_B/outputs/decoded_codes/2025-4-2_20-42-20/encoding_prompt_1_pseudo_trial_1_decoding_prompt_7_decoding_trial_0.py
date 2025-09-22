# Step 1: Input two strings from the user
firstString = input()
secondString = input()

# Step 2: Process Input
# Remove all spaces from firstString and secondString
cleanedFirst = firstString.replace(" ", "")
cleanedSecond = secondString.replace(" ", "")

# Step 3: Initialize Frequency Difference List
frequencyDifferences = []

# Step 4: Count Character Frequencies
# Loop through all characters from 'A' to 'z'
for char in range(ord('A'), ord('z') + 1):
    countInFirst = cleanedFirst.count(chr(char))  # Count in first string
    countInSecond = cleanedSecond.count(chr(char))  # Count in second string
    
    # Calculate the difference and append to the frequencyDifferences list
    frequencyDifferences.append(countInFirst - countInSecond)

# Step 5: Check Frequency Differences
# Count how many values in frequencyDifferences are less than zero
negativeCount = sum(1 for difference in frequencyDifferences if difference < 0)

# Step 6: Output Result
if negativeCount == 0:
    print("YES")  # No negative frequencies, means all characters are accounted for
else:
    print("NO")  # There are negative frequencies, some characters are lacking in the first string
