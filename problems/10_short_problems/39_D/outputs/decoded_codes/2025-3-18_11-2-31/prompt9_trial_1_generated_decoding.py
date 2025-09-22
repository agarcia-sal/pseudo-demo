# Start the Program

# Receive Input
first_set = input().split()  # Read the first set of numbers
second_set = input().split()  # Read the second set of numbers

# Initialize a Counter
difference_count = 0  # This will track how many numbers are different between the two sets

# Compare the Numbers
for index in range(3):  # Loop through indices 0 to 2
    number_from_first_set = int(first_set[index])  # Convert number from first set to integer
    number_from_second_set = int(second_set[index])  # Convert number from second set to integer
    
    # Check if the numbers at the current index are different
    if number_from_first_set != number_from_second_set:
        difference_count += 1  # Increase the counter if they are different

# Evaluate the Differences
if difference_count < 3:
    print("YES")  # Sets are similar
else:
    print("NO")  # Sets are not similar

# End the Program
