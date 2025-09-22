def main_program():
    # Step 1: Read two lines of input
    first_set = input()
    second_set = input()

    # Step 2: Split the input strings into lists of numbers
    list_first = first_set.split()
    list_second = second_set.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare each number in the two lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the current numbers from strings to integers
        number_from_first = int(list_first[index])
        number_from_second = int(list_second[index])

        # Check if the numbers are different
        if number_from_first != number_from_second:
            # Increment the difference counter
            difference_count += 1 

    # Step 5: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")   # Three or more differences

# Step 6: Execute the main program
if __name__ == "__main__":
    main_program()
