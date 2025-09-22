# Start the Program

# Step 2: Receive Input
first_set_input = input()  # Get the first set of numbers from the user
second_set_input = input()  # Get the second set of numbers from the user

# Step 3: Split Input into Individual Numbers
first_set = first_set_input.split()  # Break the first set of numbers into a list
second_set = second_set_input.split()  # Break the second set of numbers into a list

# Step 4: Initialize a Difference Counter
difference_count = 0  # Set a variable to count differences

# Step 5: Compare Corresponding Numbers
for index in range(3):  # For each index from 0 to 2 (inclusive)
    first_number = int(first_set[index])  # Convert the number from the firstSet to an integer
    second_number = int(second_set[index])  # Convert the number from the secondSet to an integer
    
    # Check if the numbers are different
    if first_number != second_number:
        difference_count += 1  # Increment the difference count if they are not equal

# Step 6: Check the Number of Differences
if difference_count < 3:  # If there are fewer than 3 differences
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise, output "NO"

# End of Program
