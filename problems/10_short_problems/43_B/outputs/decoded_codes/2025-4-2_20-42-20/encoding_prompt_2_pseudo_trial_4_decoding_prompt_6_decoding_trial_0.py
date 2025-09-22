# Step 1: Receive Input
# Taking two lines of input from the user
input_string1 = input()
input_string2 = input()

# Step 2: Remove spaces from both input strings
cleaned_string1 = input_string1.replace(" ", "")
cleaned_string2 = input_string2.replace(" ", "")

# Step 3: Initialize Frequency List
frequency_differences = []

# Step 4: Calculate Frequency Differences
for ascii_value in range(65, 123):  # Covers A-Z and a-z ASCII values
    character = chr(ascii_value)  # Convert ASCII value to character
    count_in_string1 = cleaned_string1.count(character)  # Count in first string
    count_in_string2 = cleaned_string2.count(character)  # Count in second string
    difference = count_in_string1 - count_in_string2  # Calculate the difference
    frequency_differences.append(difference)  # Store the difference

# Step 5: Check for Negative Differences
negative_differences = [diff for diff in frequency_differences if diff < 0]

# Step 6: Determine output based on the presence of negative differences
if not negative_differences:  # If there are no negative differences
    print("YES")
else:
    print("NO")
