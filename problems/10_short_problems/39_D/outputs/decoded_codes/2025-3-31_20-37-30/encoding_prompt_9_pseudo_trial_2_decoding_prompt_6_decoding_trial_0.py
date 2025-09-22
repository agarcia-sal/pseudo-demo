# Start Program

# Receive Input: Get two sets of numbers from the user
first_set = input()  # first set of numbers as a string
second_set = input()  # second set of numbers as a string

# Split Input Strings into Lists
numbers_set1 = first_set.split()  # convert first set string to a list
numbers_set2 = second_set.split()  # convert second set string to a list

# Initialize a Counter
difference_count = 0  # this will track the number of differences

# Compare Each Position
for index in range(3):  # iterate over three positions (0, 1, 2)
    # Convert values from both sets to integers
    num1 = int(numbers_set1[index])
    num2 = int(numbers_set2[index])
    
    # Check if numbers are different
    if num1 != num2:
        difference_count += 1  # increment the difference count if different

# Output the Result
if difference_count < 3:  # if differences are fewer than 3
    print("YES")
else:
    print("NO")  # if differences are 3 or more

# End Program
