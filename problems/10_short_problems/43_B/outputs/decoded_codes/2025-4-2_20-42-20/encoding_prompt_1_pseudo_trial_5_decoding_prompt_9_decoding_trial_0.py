# Read two separate lines of input strings
string1 = input()
string2 = input()

# Remove spaces from the strings
cleaned_string1 = [char for char in string1 if char != ' ']
cleaned_string2 = [char for char in string2 if char != ' ']

# Initialize Frequency Difference List
frequency_differences = []

# Calculate frequency differences
for char_code in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    char = chr(char_code)  # Convert ASCII code to character
    count_in_string1 = cleaned_string1.count(char)
    count_in_string2 = cleaned_string2.count(char)
    difference = count_in_string1 - count_in_string2
    frequency_differences.append(difference)

# Check frequency differences for negative values
negative_count = sum(1 for difference in frequency_differences if difference < 0)

# Output result
if negative_count == 0:
    print("YES")
else:
    print("NO")
