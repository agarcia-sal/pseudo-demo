def main():
    # Receive Input
    first_input = input()
    second_input = input()
    
    # Split Input into Individual Numbers
    first_set = list(map(int, first_input.split()))
    second_set = list(map(int, second_input.split()))

    # Initialize Difference Counter
    difference_count = 0

    # Compare Corresponding Items
    for index in range(3):  # Iterate over the indices 0, 1, and 2
        first_number = first_set[index]
        second_number = second_set[index]

        if first_number != second_number:
            difference_count += 1

    # Determine Result Based on Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
