# Step 1: Receive Input
# Take two lines of input from the user and clean them by removing spaces.
cleanedString1 = input().replace(" ", "")
cleanedString2 = input().replace(" ", "")

# Step 2: Initialize Frequency List
# Create a list to store the frequency differences.
frequencyDifferences = []

# Step 3: Calculate Frequency Differences
# Iterate over ASCII values for characters from 'A' (65) to 'z' (122).
for ascii_value in range(65, 123):
    # Get the character corresponding to the current ASCII value
    character = chr(ascii_value)
    
    # Count frequencies of the character in both strings
    count1 = cleanedString1.count(character)
    count2 = cleanedString2.count(character)
    
    # Calculate the difference and append to the list
    frequencyDifference = count1 - count2
    frequencyDifferences.append(frequencyDifference)

# Step 4: Check for Negative Differences
# Create a new list with only negative differences
negativeDifferences = [diff for diff in frequencyDifferences if diff < 0]

# If there are no negative differences, print "YES"; otherwise, print "NO"
if not negativeDifferences:
    print("YES")
else:
    print("NO")
