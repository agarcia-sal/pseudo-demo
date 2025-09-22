def main():
    # Step 1: Accept two lines of input from the user
    first_input = input()
    second_input = input()

    # Step 2: Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 3: Initialize a variable to count differences
    difference_count = 0 

    # Step 4: Compare corresponding elements of the two lists
    for index in range(3):  # Loop for the first three indices
        # Convert the current elements to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        # If the numbers are not equal, increment the difference count
        if first_number != second_number:
            difference_count += 1 

    # Step 5: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 6: Execute the main function when the script runs
main()
