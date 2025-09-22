# Step 1: Receive Input
first_string = input()  # Read the first string input from user
second_string = input()  # Read the second string input from user

# Step 2: Process Input to Remove Spaces
processed_first_string = [char for char in first_string if char != ' ']  # Remove spaces from first_string
processed_second_string = [char for char in second_string if char != ' ']  # Remove spaces from second_string

# Step 3: Initialize Frequency Count
frequency_differences = [0] * (ord('z') - ord('A') + 1)  # Create a list for frequency differences

# Step 4: Calculate Frequency Differences
for ascii_code in range(ord('A'), ord('z') + 1):  # Loop through ASCII values of 'A' to 'z'
    char = chr(ascii_code)  # Get the character corresponding to ASCII code
    count_first = processed_first_string.count(char)  # Count occurrences in processed_first_string
    count_second = processed_second_string.count(char)  # Count occurrences in processed_second_string
    frequency_differences[ascii_code - ord('A')] = count_first - count_second  # Store frequency difference

# Step 5: Determine Result
if all(value >= 0 for value in frequency_differences):  # Check if all values are greater than or equal to zero
    print("YES")  # If condition is met, print "YES"
else:
    print("NO")  # If any value is negative, print "NO"
