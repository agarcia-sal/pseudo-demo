# Step 1: Read Input
string1 = input()  # Read first line of input
string2 = input()  # Read second line of input

# Step 2: Remove Spaces
cleaned_string1 = []  # Create an empty list for cleaned string 1
cleaned_string2 = []  # Create an empty list for cleaned string 2

# Iterate through each character in string1 and clean it
for character in string1:
    if character != ' ':  # Check if it's not a space
        cleaned_string1.append(character)  # Add to cleaned list

# Iterate through each character in string2 and clean it
for character in string2:
    if character != ' ':  # Check if it's not a space
        cleaned_string2.append(character)  # Add to cleaned list

# Step 3: Initialize Frequency Difference List
frequency_differences = []  # Create an empty list for frequency differences

# Step 4: Calculate Frequency Differences
for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
    char_count_1 = cleaned_string1.count(chr(ascii_value))  # Count in cleaned_string1
    char_count_2 = cleaned_string2.count(chr(ascii_value))  # Count in cleaned_string2
    difference = char_count_1 - char_count_2  # Calculate difference
    frequency_differences.append(difference)  # Add difference to the list

# Step 5: Check Frequency Differences
negative_count = sum(1 for diff in frequency_differences if diff < 0)  # Count negative differences

# Step 6: Output Result
if negative_count == 0:  # If there are no negative counts
    print("YES")
else:
    print("NO")  # If there are any negative counts
