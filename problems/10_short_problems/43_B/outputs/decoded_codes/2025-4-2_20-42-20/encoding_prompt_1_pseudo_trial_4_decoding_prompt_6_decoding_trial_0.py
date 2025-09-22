# Step 1: Input two strings and remove any spaces
first_string = input().replace(" ", "")
second_string = input().replace(" ", "")

# Step 2: Create a list to hold frequency differences of characters from 'A' to 'z'
frequency_difference = []

# Step 3: Iterate over the ASCII range from 'A' (65) to 'z' (122)
for ascii_value in range(65, 123):  # ASCII values from 'A' to 'z'
    # Count how many times the character appears in each string
    char_count_in_first = first_string.count(chr(ascii_value))
    char_count_in_second = second_string.count(chr(ascii_value))
    
    # Calculate the difference and store it in the list
    difference = char_count_in_first - char_count_in_second
    frequency_difference.append(difference)

# Step 4: Check for negative differences
negative_count = sum(1 for diff in frequency_difference if diff < 0)

# Step 5: Determine if the first string has sufficient character frequencies
if negative_count == 0:
    print("YES")  # All characters in first_string are sufficient
else:
    print("NO")   # At least one character is less than required
