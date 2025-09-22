def main():
    # Step 2: Receive Input
    first_input = input()
    second_input = input()

    # Step 3: Split Input into Individual Numbers
    first_set = list(map(int, first_input.split()))
    second_set = list(map(int, second_input.split()))

    # Step 4: Initialize Difference Counter
    difference_count = 0

    # Step 5: Compare Corresponding Items
    for i in range(3):  # Since we expect exactly three integers
        first_number = first_set[i]
        second_number = second_set[i]
        if first_number != second_number:
            difference_count += 1

    # Step 6: Determine Result Based on Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Trigger the main function
if __name__ == "__main__":
    main()
