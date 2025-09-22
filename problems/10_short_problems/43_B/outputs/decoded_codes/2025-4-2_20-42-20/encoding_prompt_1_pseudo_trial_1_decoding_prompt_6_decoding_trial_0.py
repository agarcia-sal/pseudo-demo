# Step 1: Read two strings from the user
first_string = input()
second_string = input()

# Step 2: Remove all spaces from both strings
cleaned_first = first_string.replace(" ", "")
cleaned_second = second_string.replace(" ", "")

# Step 3: Initialize an empty list to store frequency differences
frequency_differences = []

# Step 4: Count character frequencies from 'A' to 'z'
for char in range(ord('A'), ord('z') + 1):
    count_in_first = cleaned_first.count(chr(char))
    count_in_second = cleaned_second.count(chr(char))
    
    # Calculate the frequency difference and append to the list
    frequency_difference = count_in_first - count_in_second
    frequency_differences.append(frequency_difference)

# Step 5: Check how many values are less than zero
negative_count = sum(1 for diff in frequency_differences if diff < 0)

# Step 6: Output result based on negative count
if negative_count == 0:
    print("YES")
else:
    print("NO")
