# Start the program

# Define the main function
def main():
    # Read input from the user
    first_input = input()  # Store the first input line
    second_input = input()  # Store the second input line

    # Split the first input into separate elements and store them in a list called first_list
    first_list = first_input.split()
    # Split the second input into separate elements and store them in a list called second_list
    second_list = second_input.split()

    # Initialize a variable called difference_count to zero
    difference_count = 0

    # For each index from 0 to 2
    for index in range(3):
        # Convert the element from first_list at the current index into an integer
        first_value = int(first_list[index])
        # Convert the element from second_list at the current index into an integer
        second_value = int(second_list[index])
        
        # If first_value is not equal to second_value
        if first_value != second_value:
            # Increment difference_count by 1
            difference_count += 1

    # If difference_count is less than 3
    if difference_count < 3:
        # Output "YES"
        print("YES")
    # Otherwise
    else:
        # Output "NO"
        print("NO")

# Execute the main function when the program runs
main()
