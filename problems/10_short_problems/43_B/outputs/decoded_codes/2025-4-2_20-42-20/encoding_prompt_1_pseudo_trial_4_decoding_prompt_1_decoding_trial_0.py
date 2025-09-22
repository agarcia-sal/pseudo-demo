# Step 1: Input Two Strings
s1 = input().replace(" ", "")  # Read the first string and remove spaces
s2 = input().replace(" ", "")  # Read the second string and remove spaces

# Step 2: Create Character Frequency Difference
frequency_differences = []  # Initialize a list to hold frequency differences

for char in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    count_s1 = s1.count(chr(char))  # Count occurrences in first string
    count_s2 = s2.count(chr(char))  # Count occurrences in second string
    difference = count_s1 - count_s2  # Calculate frequency difference
    frequency_differences.append(difference)  # Store difference in list

# Step 3: Check for Negative Differences
negative_count = sum(1 for diff in frequency_differences if diff < 0)  # Count negative differences

if negative_count == 0:  # Check if there are no negative differences
    print("YES")  # All characters in s1 are >= in s2
else:
    print("NO")  # At least one character in s2 has a greater count
