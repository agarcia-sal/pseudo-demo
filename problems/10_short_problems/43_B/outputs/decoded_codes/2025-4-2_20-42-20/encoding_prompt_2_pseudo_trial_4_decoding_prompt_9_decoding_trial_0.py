# Receive input
string1 = input()
string2 = input()

# Remove spaces from both strings
cleanedString1 = string1.replace(" ", "")
cleanedString2 = string2.replace(" ", "")

# Initialize frequency list
frequencyDifferences = []

# Calculate frequency differences for ASCII values from 'A' (65) to 'z' (122)
for ascii_value in range(65, 123):
    # Count occurrences of the character in both cleaned strings
    countInString1 = cleanedString1.count(chr(ascii_value))
    countInString2 = cleanedString2.count(chr(ascii_value))
    
    # Calculate the difference
    difference = countInString1 - countInString2
    # Append the difference to the frequencyDifferences list
    frequencyDifferences.append(difference)

# Check for negative differences
negativeDifferences = [diff for diff in frequencyDifferences if diff < 0]

# Output result based on the existence of negative differences
if len(negativeDifferences) == 0:
    print("YES")
else:
    print("NO")
