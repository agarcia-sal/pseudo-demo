# Program to compare two sets of three numbers and count the differences

# Step 1: Gather input
first_numbers = input()  # Record first set of numbers as a string of space-separated values
second_numbers = input()  # Record second set of numbers as a string of space-separated values

# Step 2: Split the input strings into lists of numbers
first_list = first_numbers.split()  # Split first set into a list
second_list = second_numbers.split()  # Split second set into a list

# Step 3: Initialize a counter for differences
difference_count = 0 

# Step 4: Compare corresponding numbers in both lists
for index in range(3):  # Loop through the first three elements
    # Convert the values to integers for comparison
    num_a = int(first_list[index])  # Convert element from the first list to integer
    num_b = int(second_list[index])  # Convert element from the second list to integer

    # Step 5: Check if the numbers are different
    if num_a != num_b:  # If the numbers are not equal
        difference_count += 1  # Increment the difference count

# Step 6: Determine the output based on the number of differences
if difference_count < 3:  # If less than three differences
    print("YES")  # Output YES
else:  # If three or more differences
    print("NO")  # Output NO
