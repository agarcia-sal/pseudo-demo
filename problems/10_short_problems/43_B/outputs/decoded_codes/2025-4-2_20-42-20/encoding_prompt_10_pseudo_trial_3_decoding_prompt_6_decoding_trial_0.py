# Begin Program

# Step 2: Initialize two lists to hold characters from the inputs
list_first_input = []
list_second_input = []

# Step 4: Read inputs from the user
first_input = input()
second_input = input()

# Step 6: Process first input to filter out spaces
for character in first_input:
    if character != ' ':
        list_first_input.append(character)

# Step 7: Process second input to filter out spaces
for character in second_input:
    if character != ' ':
        list_second_input.append(character)

# Step 8: Initialize a list to store frequency differences
frequency_differences = []

# Step 9: Calculate frequency differences for characters 'A' to 'z'
for ascii_value in range(ord('A'), ord('z') + 1):
    count_in_first_input = list_first_input.count(chr(ascii_value))
    count_in_second_input = list_second_input.count(chr(ascii_value))
    frequency_difference = count_in_first_input - count_in_second_input
    frequency_differences.append(frequency_difference)

# Step 10: Count the number of elements in frequency_differences that are less than 0
count_negatives = sum(1 for difference in frequency_differences if difference < 0)

# Step 11: Output the result based on the count of negative differences
if count_negatives == 0:
    print("YES")
else:
    print("NO")

# End Program
