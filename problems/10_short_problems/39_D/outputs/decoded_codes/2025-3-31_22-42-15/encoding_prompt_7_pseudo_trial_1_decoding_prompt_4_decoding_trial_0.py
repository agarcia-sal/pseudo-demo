def do_main():
    # Read input values
    first_input = input()  # Input format: "number number number"
    second_input = input()  # Input format: "number number number"

    # Split inputs into lists of strings
    list1 = first_input.split()
    list2 = second_input.split()

    # Initialize a variable to count differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        value_a = int(list1[index])
        value_b = int(list2[index])

        # Check if the two values are different
        if value_a != value_b:
            # Increment the count of differences
            difference_count += 1

    # Check the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")


# Execution starts here
if __name__ == "__main__":
    do_main()
