# Start of the program

# Receive two input strings representing sets of three numbers
first_set = input()
second_set = input()

# Split both input strings into lists of numbers
numbers_first = first_set.split()
numbers_second = second_set.split()

# Initialize a counter for differences
difference_count = 0

# Loop through each number in both lists to compare them
for index in range(3):
    # Convert the numbers from string to integer
    num_first = int(numbers_first[index])
    num_second = int(numbers_second[index])
    
    # If the numbers are not equal, increase the difference count
    if num_first != num_second:
        difference_count += 1

# Evaluate the number of differences
if difference_count < 3:
    print("YES")
else:
    print("NO")

# End of the program
