def do_main():
    # Step 1: Read input
    first_input = input()
    second_input = input()

    # Step 2: Split the inputs into lists
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 3: Initialize a counter to track differences
    difference_count = 0

    # Step 4: Compare elements in both lists
    for index in range(3):
        # Convert string elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # If the elements are not equal, increment the counter
        if first_value != second_value:
            difference_count += 1

    # Step 5: Determine and output the result based on the counter
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Program Execution Start
do_main()
