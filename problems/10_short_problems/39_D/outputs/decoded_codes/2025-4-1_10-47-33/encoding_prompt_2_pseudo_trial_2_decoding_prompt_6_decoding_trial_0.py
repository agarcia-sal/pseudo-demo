# Start the program

# Receive input
first_input = input()  # Read the first line of input
second_input = input()  # Read the second line of input

# Process the inputs
first_list = first_input.split()  # Split the first input into a list of strings
second_list = second_input.split()  # Split the second input into a list of strings
difference_count = 0  # Initialize a variable to track the number of differing elements

# Compare elements
for index in range(3):  # Loop through indices 0 to 2
    first_number = int(first_list[index])  # Convert the current element to integer from the first list
    second_number = int(second_list[index])  # Convert the current element to integer from the second list
    if first_number != second_number:  # If the numbers are not equal
        difference_count += 1  # Increment the difference count by 1

# Evaluate the results
if difference_count < 3:  # If fewer than 3 differences
    print("YES")  # Output "YES"
else:  # If 3 or more differences
    print("NO")  # Output "NO"

# End the program
