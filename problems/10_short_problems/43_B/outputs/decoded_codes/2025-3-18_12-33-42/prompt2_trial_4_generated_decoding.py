# Step 1: Receive Input
first_input_string = input()
second_input_string = input()

# Step 2: Process Inputs
processed_first_input = [char for char in first_input_string if char != ' ']
processed_second_input = [char for char in second_input_string if char != ' ']

# Step 3: Calculate Frequency Difference
frequency_differences = []

# ASCII values of 'A' to 'Z' and 'a' to 'z' range from 65 to 122
for char_code in range(65, 123):  # 65 is 'A' and 122 is 'z'
    char = chr(char_code)
    count_first = processed_first_input.count(char)
    count_second = processed_second_input.count(char)
    frequency_differences.append(count_first - count_second)

# Step 4: Determine Output
if any(diff < 0 for diff in frequency_differences):
    print("NO")
else:
    print("YES")
