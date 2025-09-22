# Start of the main function

# Input Phase:
# Prompt user for the first sequence of three numbers
first_sequence = input()  # User inputs a sequence like "1 2 3"
# Prompt user for the second sequence of three numbers
second_sequence = input()  # User inputs another sequence like "1 2 4"

# Process Input:
# Split the first sequence into a list of strings
first_list = first_sequence.split()
# Split the second sequence into a list of strings
second_list = second_sequence.split()

# Initialize Difference Counter:
# Set the counter to zero to track differences
difference_count = 0

# Comparison Loop:
# Iterate over the range of three positions
for i in range(3):
    # Convert the numbers from each list to integers
    number_from_first = int(first_list[i])
    number_from_second = int(second_list[i])
    
    # Check if the numbers are different
    if number_from_first != number_from_second:
        # Increment the difference count
        difference_count += 1

# Decision-making:
# Check the number of differences found
if difference_count < 3:
    # If differences are less than 3, print YES
    print("YES")
else:
    # If differences are 3 or more, print NO
    print("NO")

# End of the main function
