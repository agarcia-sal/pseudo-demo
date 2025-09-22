# Input Two Strings
s1 = input().replace(" ", "")
s2 = input().replace(" ", "")

# Create Character Frequency Difference
frequency_diff = []

# Loop through ASCII range from 'A' (65) to 'z' (122)
for char in range(65, 123):
    count_s1 = s1.count(chr(char))  # Count in the first string
    count_s2 = s2.count(chr(char))  # Count in the second string
    difference = count_s1 - count_s2  # Calculate the difference
    frequency_diff.append(difference)  # Store the difference in the list

# Check for Negative Differences
negative_count = sum(1 for diff in frequency_diff if diff < 0)  # Count how many are negative

# Output based on the negative count
if negative_count == 0:
    print("YES")
else:
    print("NO")
