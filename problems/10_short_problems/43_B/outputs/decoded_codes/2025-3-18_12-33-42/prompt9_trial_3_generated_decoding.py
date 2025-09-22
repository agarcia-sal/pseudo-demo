# Receive user input for two strings
first_string = input()
second_string = input()

# Process input strings: remove spaces
first_string_no_spaces = first_string.replace(" ", "")
second_string_no_spaces = second_string.replace(" ", "")

# Initialize frequency comparison list
frequency_difference = []

# Calculate the character frequencies from 'A' to 'z'
for char in range(ord('A'), ord('z') + 1):
    char = chr(char)
    count_first_string = first_string_no_spaces.count(char)
    count_second_string = second_string_no_spaces.count(char)
    
    # Calculate the difference in frequency
    difference = count_first_string - count_second_string
    frequency_difference.append(difference)

# Evaluate frequency differences
negative_count = sum(1 for diff in frequency_difference if diff < 0)

# Generate output based on the negative count
if negative_count == 0:
    print("YES")  # The first string has sufficient characters
else:
    print("NO")   # The first string does not have sufficient characters
