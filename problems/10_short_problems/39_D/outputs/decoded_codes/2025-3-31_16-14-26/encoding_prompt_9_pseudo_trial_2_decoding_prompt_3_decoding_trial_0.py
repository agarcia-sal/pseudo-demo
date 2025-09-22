def main():
    # Step 1: Receive input
    first_set = input()  # Prompt user for first set of three numbers
    second_set = input()  # Prompt user for second set of three numbers

    # Step 2: Split the input strings into lists
    numbers_from_first_set = first_set.split()
    numbers_from_second_set = second_set.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare the numbers in both sets
    for index in range(3):
        # Convert string inputs to integers
        number_from_first = int(numbers_from_first_set[index])
        number_from_second = int(numbers_from_second_set[index])

        # Step 5: Check if the numbers are different
        if number_from_first != number_from_second:
            # Increment difference count by 1 if they are different
            difference_count += 1

    # Step 6: Evaluate the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function
if __name__ == "__main__":
    main()


Input:
1 2 3
1 2 4
Output:
YES


Input:
1 2 3
4 5 6
Output:
NO
