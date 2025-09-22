def main():
    # Step 1: Obtain input from the user
    first_input = input()  # first set of input values
    second_input = input()  # second set of input values

    # Step 4: Split the inputs into lists of values
    first_values = first_input.split()
    second_values = second_input.split()

    # Step 6: Initialize a variable to count discrepancies
    discrepancy_count = 0

    # Step 7: Check the first three values for discrepancies
    for index in range(3):  # We are only checking the first three indices
        value_from_first = int(first_values[index])  # Convert to integer
        value_from_second = int(second_values[index])  # Convert to integer

        # Compare the two values
        if value_from_first != value_from_second:
            discrepancy_count += 1  # Increment discrepancy count if values are different

    # Step 8: Determine the result based on discrepancy count
    if discrepancy_count < 3:
        print("YES")  # Output YES if discrepancies are less than 3
    else:
        print("NO")  # Output NO if there are 3 or more discrepancies

# Step 9: Call the main function to execute the program
if __name__ == "__main__":
    main()
