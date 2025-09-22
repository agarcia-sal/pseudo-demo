def main():
    # Step 1: Receive input
    first_set = input()  # first set of three numbers
    second_set = input()  # second set of three numbers

    # Step 2: Split the input strings into lists
    numbers_from_first_set = first_set.split()
    numbers_from_second_set = second_set.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare the numbers in both sets
    for index in range(3):  # Step 4: Loop through the first three indices
        # Convert the numbers to integers
        number_from_first = int(numbers_from_first_set[index])
        number_from_second = int(numbers_from_second_set[index])

        # Step 5: Check if the numbers are different
        if number_from_first != number_from_second:
            difference_count += 1  # Increment the difference count

    # Step 6: Evaluate the number of differences
    if difference_count < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO if differences are 3 or more

# Step 7: Execute the main function
main()
