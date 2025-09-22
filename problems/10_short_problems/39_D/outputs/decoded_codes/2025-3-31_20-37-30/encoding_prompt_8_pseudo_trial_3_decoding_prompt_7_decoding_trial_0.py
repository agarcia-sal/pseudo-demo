def main_program():
    # Step 1: Read two lines of input
    first_set = input()  # Get first set of numbers as a string
    second_set = input()  # Get second set of numbers as a string

    # Step 2: Split the input strings into lists of numbers
    list_first = first_set.split()  # Split the first set by spaces
    list_second = second_set.split()  # Split the second set by spaces

    # Step 3: Initialize a counter for differences
    difference_count = 0  # Counter to track the number of differences

    # Step 4: Compare each number in the two lists
    for index in range(3):  # Iterate over the indices 0 to 2
        # Convert the current numbers from strings to integers
        number_from_first = int(list_first[index])  # Convert to integer
        number_from_second = int(list_second[index])  # Convert to integer

        # Check if the numbers are different
        if number_from_first != number_from_second:  # If numbers do not match
            # Increment the difference counter
            difference_count += 1  # Increment the difference count

    # Step 5: Determine the output based on the number of differences
    if difference_count < 3:  # If the count of differences is less than 3
        print("YES")  # Output YES if less than three differences
    else:
        print("NO")  # Output NO if three or more differences

# Step 6: Execute the main program
if __name__ == "__main__":  # Check if this is the main program
    main_program()  # Call the main program function
