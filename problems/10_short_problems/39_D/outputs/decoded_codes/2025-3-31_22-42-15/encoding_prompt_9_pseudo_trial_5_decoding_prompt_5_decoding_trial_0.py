# Start the main process.

# Receive Input
first_set = input()  # Read the first line of input
second_set = input()  # Read the second line of input

# Split Input into Lists
first_list = first_set.split()  # Split firstSet into a list of strings
second_list = second_set.split()  # Split secondSet into a list of strings

# Initialize a Counter
difference_count = 0  # This will track the number of positions where the values differ

# Compare Corresponding Values
for index in range(3):  # Loop through indices 0 to 2
    value_from_first = int(first_list[index])  # Convert value at index from firstList to int
    value_from_second = int(second_list[index])  # Convert value at index from secondList to int
    if value_from_first != value_from_second:  # If values differ
        difference_count += 1  # Increment the difference count

# Evaluate the Result
if difference_count < 3:
    print("YES")  # Print "YES" if differences are less than 3
else:
    print("NO")  # Print "NO" otherwise

# End the main process.
