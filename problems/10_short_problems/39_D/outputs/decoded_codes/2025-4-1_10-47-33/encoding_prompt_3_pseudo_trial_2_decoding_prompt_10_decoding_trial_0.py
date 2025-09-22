def do_main():
    # Step 1: Read two lines of input
    first_input = input()
    second_input = input()

    # Step 2: Split the inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        # Step 5: Compare the two numbers
        if first_number != second_number:
            difference_count += 1

    # Step 6: Check the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    do_main()
