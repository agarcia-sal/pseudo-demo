# Start Main Program

# Receive Input
first_set = input()
second_set = input()

# Split Input into Individual Numbers
first_list = first_set.split()  # Convert first input into a list of strings
second_list = second_set.split()  # Convert second input into a list of strings

# Initialize Count of Differences
difference_count = 0  # Initialize the difference counter

# Compare Corresponding Numbers
for index in range(3):  # Loop through indices 0, 1, 2
    first_number = int(first_list[index])  # Convert string to integer
    second_number = int(second_list[index])  # Convert string to integer
    
    # If numbers differ, increment the difference count
    if first_number != second_number:
        difference_count += 1

# Evaluate Results
if difference_count < 3:
    print("YES")  # Sets differ in fewer than three places
else:
    print("NO")  # Sets differ in three or more places

# End Main Program
