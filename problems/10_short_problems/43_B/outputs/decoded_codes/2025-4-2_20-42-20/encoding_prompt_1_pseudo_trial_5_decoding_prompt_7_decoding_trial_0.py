# Step 1: Read Input
String1 = input()  # Reading the first string
String2 = input()  # Reading the second string

# Step 2: Remove Spaces
# Create lists to hold characters without spaces
CleanedString1 = [char for char in String1 if char != ' ']  # List comprehension to remove spaces from String1
CleanedString2 = [char for char in String2 if char != ' ']  # List comprehension to remove spaces from String2

# Step 3: Initialize Frequency Difference List
FrequencyDifferences = []  # List to hold the frequency differences

# Step 4: Calculate Frequency Differences
# Loop through character codes from ASCII 'A' (65) to 'z' (122)
for char_code in range(65, 123):  # ASCII range from A to z
    # Convert ASCII code back to character
    char = chr(char_code)
    
    # Count occurrences in both cleaned strings
    count1 = CleanedString1.count(char)  # Count of char in CleanedString1
    count2 = CleanedString2.count(char)  # Count of char in CleanedString2
    
    # Calculate the frequency difference
    frequency_difference = count1 - count2
    FrequencyDifferences.append(frequency_difference)  # Append the difference to the list

# Step 5: Check Frequency Differences
# Count how many values in FrequencyDifferences are negative
negative_count = sum(1 for diff in FrequencyDifferences if diff < 0)  # Count how many differences are negative

# Step 6: Output Result
# Determine the output based on the count of negative differences
if negative_count == 0:
    print("YES")  # If there are no negative differences
else:
    print("NO")   # If there are negative differences
