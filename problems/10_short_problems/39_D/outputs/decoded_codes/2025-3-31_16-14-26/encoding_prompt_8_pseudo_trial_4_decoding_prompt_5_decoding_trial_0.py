def main_procedure():
    # Step 1: Accept two lines of input from the user
    first_input = input()  # User input for the first set of numbers
    second_input = input()  # User input for the second set of numbers

    # Step 2: Split the input strings into lists of strings
    first_list = first_input.split()  # Split first input into list
    second_list = second_input.split()  # Split second input into list

    # Step 3: Initialize a counter to track the number of differences
    difference_count = 0

    # Step 4: Compare the numbers in both lists
    for index in range(3):  # Only comparing the first three elements
        # Convert current elements to integers for comparison
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        # Check if the numbers are not equal
        if first_number != second_number:
            # Increment the difference counter
            difference_count += 1

    # Step 5: Determine the outcome based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main procedure when the program runs
main_procedure()
