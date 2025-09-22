# Initialize lists to store the input strings without spaces
first_input = list(input().replace(" ", ""))
second_input = list(input().replace(" ", ""))

# List to store the difference in character counts
character_frequency_difference = []

# Count character frequencies
for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
    char = chr(ascii_value)
    count_in_first = first_input.count(char)
    count_in_second = second_input.count(char)
    
    # Calculate the difference in counts
    difference = count_in_first - count_in_second
    character_frequency_difference.append(difference)

# Evaluate results based on differences
negative_count = sum(1 for diff in character_frequency_difference if diff < 0)

# Output the result based on negative counts
if negative_count == 0:
    print("YES")
else:
    print("NO")
