# Step 1: Receive Input
first_string = input()  # Obtain first string from user
second_string = input()  # Obtain second string from user

# Step 2: Process Input Strings
first_processed = first_string.replace(" ", "")  # Remove spaces from first string
second_processed = second_string.replace(" ", "")  # Remove spaces from second string

# Step 3: Initialize Frequency List
frequency_difference = [0] * 256  # List to hold frequency differences for ASCII characters

# Step 4: Calculate Character Frequencies
for char in range(65, 123):  # ASCII values from 'A'(65) to 'z'(122)
    count_first = first_processed.count(chr(char))  # Count character in first processed string
    count_second = second_processed.count(chr(char))  # Count character in second processed string
    frequency_difference[char] = count_first - count_second  # Calculate difference

# Step 5: Check Conditions
# Count how many values in frequency_difference are negative
negative_count = sum(1 for diff in frequency_difference if diff < 0)

if negative_count == 0:
    print("YES")  # All characters in firstProcessed meet or exceed counts in secondProcessed
else:
    print("NO")  # Some characters in secondProcessed exceed those in firstProcessed
