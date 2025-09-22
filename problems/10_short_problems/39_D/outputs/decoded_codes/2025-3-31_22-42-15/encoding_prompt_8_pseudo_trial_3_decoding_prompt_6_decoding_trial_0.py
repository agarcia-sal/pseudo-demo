def main():
    # Step 1: Gather user input
    first_set = input()  # Read first set of numbers
    second_set = input()  # Read second set of numbers

    # Step 2: Split the input strings into individual numbers
    first_numbers = first_set.split()  # Split the first set into a list
    second_numbers = second_set.split()  # Split the second set into a list

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare each number in the two sets
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the current numbers from string to integer
        number_from_first_set = int(first_numbers[index])  # Convert to integer
        number_from_second_set = int(second_numbers[index])  # Convert to integer

        # Check if the numbers are different
        if number_from_first_set != number_from_second_set:  # If numbers are different
            # Increment the count of differences
            difference_count += 1

    # Step 5: Determine the output based on the count of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")
    else:
        print("NO")  # If differences are 3 or more

# Entry point of the program
main()  # Call the main function
