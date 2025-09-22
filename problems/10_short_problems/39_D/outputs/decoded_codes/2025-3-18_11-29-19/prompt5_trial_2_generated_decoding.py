def perform_comparison():
    # Accept two sets of numbers as input
    first_input = input()  # Get the first set of numbers from the user
    second_input = input()  # Get the second set of numbers from the user

    # Split the input strings into lists of numbers
    first_set = first_input.split()  # Convert the first input string into a list of numbers
    second_set = second_input.split()  # Convert the second input string into a list of numbers

    # Initialize a counter for the differences
    difference_counter = 0 

    # Iterate through each number in the sets
    for index in range(3):  # We assume the inputs will always contain exactly 3 numbers
        # Convert the string numbers to integers
        first_number = int(first_set[index])  # Get the number from the first set
        second_number = int(second_set[index])  # Get the number from the second set
        
        # Check if the numbers are different
        if first_number != second_number:
            difference_counter += 1  # Increase the difference counter if they are not the same

    # Check the total number of differences
    if difference_counter < 3:
        print("YES")  # Output YES if less than three differences found
    else:
        print("NO")  # Output NO if three or more differences found

# Entry point of the program
if __name__ == "__main__":
    perform_comparison()  # Execute the comparison function
