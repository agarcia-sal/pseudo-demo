# Read Input Strings
firstString = input().replace(" ", "")
secondString = input().replace(" ", "")

# Initialize Character Frequency Difference
frequencyDifferences = []

# Calculate Frequency Differences
for ascii_value in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    char = chr(ascii_value)  # Get character from ASCII value
    count_first = firstString.count(char)  # Count occurrences in firstString
    count_second = secondString.count(char)  # Count occurrences in secondString
    difference = count_first - count_second  # Calculate frequency difference
    frequencyDifferences.append(difference)  # Append to the list

# Determine If Strings Are Equivalent
negative_count = sum(1 for diff in frequencyDifferences if diff < 0)  # Count negative values

# Produce Output
if negative_count == 0:
    print("YES")
else:
    print("NO")
