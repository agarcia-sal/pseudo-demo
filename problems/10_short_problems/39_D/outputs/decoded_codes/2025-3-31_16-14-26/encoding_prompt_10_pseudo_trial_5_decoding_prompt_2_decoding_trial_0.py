def main():
    # Step 1: Read two lines of input
    first_input = input()
    second_input = input()

    # Step 2: Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 3: Initialize a variable to count differences
    difference_count = 0

    # Step 4: Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Step 5: Check for differences between the elements
        if first_value != second_value:
            difference_count += 1  # INCREMENT differenceCount BY 1

    # Step 6: Check the count of differences to decide output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# If this file is executed as main then
if __name__ == "__main__":
    main()
