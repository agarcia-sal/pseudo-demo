# Step 1: Input two strings
first_string = input()  # Read the first string from the user
second_string = input()  # Read the second string from the user

# Step 2: Process the strings to remove spaces
# Create new strings that include only characters that are not spaces
first_processed = first_string.replace(" ", "")  # Remove spaces in the first string
second_processed = second_string.replace(" ", "")  # Remove spaces in the second string

# Step 3: Initialize a frequency list
# Create an empty list to store frequency differences for each character from 'A' to 'z'
frequency_diff = [0] * (ord('z') - ord('A') + 1)  # List to hold frequency differences

# Step 4: Calculate the frequency difference
for char in range(ord('A'), ord('z') + 1):  # Iterate over character range from 'A' to 'z'
    # Count occurrences in each string
    count_first = first_processed.count(chr(char))  # Count in first string
    count_second = second_processed.count(chr(char))  # Count in second string
    
    # Calculate the frequency difference
    frequency_diff[char - ord('A')] = count_first - count_second  # Store difference in the list

# Step 5: Check the frequency list for negative values
# Count how many values in the frequency list are less than zero
negative_count = sum(1 for value in frequency_diff if value < 0)  # Counting negative values

# Step 6: Output the result
if negative_count == 0:  # If there are no negative values
    print("YES")  # Print "YES"
else:  # If there is at least one negative value
    print("NO")  # Print "NO"
