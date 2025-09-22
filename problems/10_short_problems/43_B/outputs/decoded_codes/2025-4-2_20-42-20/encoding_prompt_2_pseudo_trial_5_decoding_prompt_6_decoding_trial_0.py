# Step 1: Get Input
first_string = input()  # Read the first string
second_string = input()  # Read the second string

# Step 2: Process Input
processed_first_string = []  # List for processed characters from the first string
processed_second_string = []  # List for processed characters from the second string

# Add non-space characters of the first string to processed_first_string
for character in first_string:
    if character != ' ':
        processed_first_string.append(character)

# Add non-space characters of the second string to processed_second_string
for character in second_string:
    if character != ' ':
        processed_second_string.append(character)

# Step 3: Frequency Calculation
frequency_differences = []  # List to store frequency differences

# Check frequency from ASCII value of 'A' (65) to 'z' (122)
for ascii_code in range(65, 123):  # From 'A' to 'z'
    first_count = processed_first_string.count(chr(ascii_code))  # Count in first string
    second_count = processed_second_string.count(chr(ascii_code))  # Count in second string
    frequency_difference = first_count - second_count  # Calculate the difference
    frequency_differences.append(frequency_difference)  # Store the difference

# Step 4: Condition Check and Output
if any(difference < 0 for difference in frequency_differences):  # If there's any negative value
    print("NO")
else:
    print("YES")  # No negatives found
