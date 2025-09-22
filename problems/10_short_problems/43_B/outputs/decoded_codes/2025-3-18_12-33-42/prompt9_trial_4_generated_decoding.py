# Initialize Two Input Strings
firstString = input()
secondString = input()

# Clean the Strings by removing spaces
firstString = firstString.replace(" ", "")
secondString = secondString.replace(" ", "")

# Create a list to hold frequency differences for each character
frequencyDifferences = []

# Count Character Frequencies for characters from 'A' (ASCII 65) to 'z' (ASCII 122)
for ascii_value in range(65, 123):
    character = chr(ascii_value)
    countInFirstString = firstString.count(character)
    countInSecondString = secondString.count(character)
    
    # Calculate the difference in counts
    difference = countInFirstString - countInSecondString
    
    # Store the difference in frequencyDifferences
    frequencyDifferences.append(difference)

# Check Frequency Differences
negativeCount = sum(1 for difference in frequencyDifferences if difference < 0)

# Output Result
if negativeCount == 0:
    print("YES")
else:
    print("NO")
