def main():
    # Step 1: Receive input for the first set of integers
    print("Enter the first set of integers:")
    first_set = input()  # User input for the first set of integers

    # Step 2: Receive input for the second set of integers
    print("Enter the second set of integers:")
    second_set = input()  # User input for the second set of integers

    # Step 3: Split the input into individual integers
    first_set_list = first_set.split()  # Convert the input string into a list of strings
    second_set_list = second_set.split()  # Convert the input string into a list of strings

    # Step 4: Initialize a counter for differences
    difference_count = 0  # Count the number of differing integers

    # Step 5: Compare corresponding integers in both sets
    for index in range(3):  # Looping through the first three indices (0 to 2)
        # Convert the current string values to integers
        first_value = int(first_set_list[index])  # Convert to integer
        second_value = int(second_set_list[index])  # Convert to integer
        
        # Step 6: Check if the integers are different
        if first_value != second_value:  # Compare the integer values
            difference_count += 1  # Increment the difference count if they are not equal

    # Step 7: Determine if the two sets are considered similar
    if difference_count < 3:  # Check if the count of differences is less than 3
        print("YES")  # Print YES if similar
    else:
        print("NO")  # Print NO if not similar

# Step 8: Execute the main function when the script runs
main()  # Call the main function
