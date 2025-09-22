# Step 1: Input two strings
first_string = input()
second_string = input()

# Step 2: Process the strings to remove spaces
first_string_processed = ''.join(c for c in first_string if c != ' ')
second_string_processed = ''.join(c for c in second_string if c != ' ')

# Step 3: Initialize a frequency list
frequency_difference = [0] * (ord('z') - ord('A') + 1)

# Step 4: Calculate the frequency difference
for c in range(ord('A'), ord('z') + 1):
    count_first = first_string_processed.count(chr(c))
    count_second = second_string_processed.count(chr(c))
    frequency_difference[c - ord('A')] = count_first - count_second

# Step 5: Check the frequency list for negative values
negative_count = sum(1 for value in frequency_difference if value < 0)

# Step 6: Output the result
if negative_count == 0:
    print("YES")
else:
    print("NO")


def calculate_frequency_difference(first_string, second_string):
    # Remove spaces
    cleaned_first_string = ''.join(c for c in first_string if c != ' ')
    cleaned_second_string = ''.join(c for c in second_string if c != ' ')

    # Initialize frequency counts
    frequency_count = [0] * (ord('z') - ord('A') + 1)

    # Count frequencies for both strings
    for char in cleaned_first_string:
        frequency_count[ord(char) - ord('A')] += 1
    for char in cleaned_second_string:
        frequency_count[ord(char) - ord('A')] -= 1

    # Check for negative values
    if any(count < 0 for count in frequency_count):
        return "NO"
    return "YES"

# Input two strings
first_string = input()
second_string = input()

# Output the result
print(calculate_frequency_difference(first_string, second_string))
