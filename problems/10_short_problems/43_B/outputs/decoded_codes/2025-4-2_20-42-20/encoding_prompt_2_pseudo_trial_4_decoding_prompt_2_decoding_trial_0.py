# Receive Input
cleanedString1 = input().replace(" ", "")
cleanedString2 = input().replace(" ", "")

# Initialize Frequency List
frequencyDifferences = []

# Calculate Frequency Differences
for i in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    char = chr(i)
    countInString1 = cleanedString1.count(char)  # Count occurrences in cleanedString1
    countInString2 = cleanedString2.count(char)  # Count occurrences in cleanedString2
    
    # Calculate the difference
    difference = countInString1 - countInString2
    
    # Store the difference in frequencyDifferences list
    frequencyDifferences.append(difference)

# Check for Negative Differences
negativeDifferences = [diff for diff in frequencyDifferences if diff < 0]

if not negativeDifferences:  # If there are no negative differences
    print("YES")
else:
    print("NO")
