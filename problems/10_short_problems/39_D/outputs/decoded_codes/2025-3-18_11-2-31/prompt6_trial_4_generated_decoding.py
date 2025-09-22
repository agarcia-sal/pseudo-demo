def main():
    # Step 1: Read two lines of input from the user
    first_line = input()
    second_line = input()

    # Step 2: Split the input lines into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Loop through the first three elements of each list
    for index in range(3):
        # Convert the current elements from strings to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Step 5: Compare the two values
        if first_value != second_value:
            # Increment the difference counter if values are different
            difference_count += 1

    # Step 6: Check the number of differences found
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function when the program runs
main()
