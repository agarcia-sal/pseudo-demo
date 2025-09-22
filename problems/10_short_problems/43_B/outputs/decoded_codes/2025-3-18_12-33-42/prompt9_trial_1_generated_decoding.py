# Receive Input
first_string = input().replace(" ", "")
second_string = input().replace(" ", "")

# Prepare Character Frequency Count
frequency_differences_list = []

# Iterate through character set from 'A' to 'z'
for char in range(ord('A'), ord('z') + 1):
    count_in_first = first_string.count(chr(char))
    count_in_second = second_string.count(chr(char))
    
    # Calculate the difference in frequency
    frequency_difference = count_in_first - count_in_second
    frequency_differences_list.append(frequency_difference)

# Evaluate Character Frequencies
negative_count = sum(1 for difference in frequency_differences_list if difference < 0)

# Results
if negative_count == 0:
    print("YES")  # Both strings have the same character frequencies
else:
    print("NO")   # There is a mismatch in character frequencies
