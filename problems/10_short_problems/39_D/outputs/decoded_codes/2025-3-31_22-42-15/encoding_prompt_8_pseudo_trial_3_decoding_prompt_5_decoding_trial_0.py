def main():
    # Step 1: Gather user input
    print("Enter first set of numbers:")
    first_set = input()
    print("Enter second set of numbers:")
    second_set = input()

    # Step 2: Split the input strings into individual numbers
    first_numbers = first_set.split()
    second_numbers = second_set.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare each number in the two sets
    for index in range(3):  # Assuming we are only interested in the first 3 numbers
        # Convert the current numbers from string to integer
        number_from_first_set = int(first_numbers[index])
        number_from_second_set = int(second_numbers[index])

        # Check if the numbers are different
        if number_from_first_set != number_from_second_set:
            # Increment the count of differences
            difference_count += 1

    # Step 5: Determine the output based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
main()
