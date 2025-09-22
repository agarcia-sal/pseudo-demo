# Start of the main function

# Step 1: Accept input for two sequences of three integers
first_sequence = input()
second_sequence = input()

# Step 2: Split the input strings into lists of integers
first_list = first_sequence.split()
second_list = second_sequence.split()

# Step 3: Initialize a counter for differences
difference_count = 0

# Step 4: Compare integers in both lists
for index in range(3):  # We are comparing 3 elements
    # Convert the string elements to integers
    first_number = int(first_list[index])
    second_number = int(second_list[index])
    
    # Step 5: If numbers are different, increment the counter
    if first_number != second_number:
        difference_count += 1

# Step 6: Determine if the difference count is less than three
if difference_count < 3:
    print("YES")
else:
    print("NO")

# End of the main function
