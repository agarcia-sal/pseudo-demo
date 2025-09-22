def main():
    # Step 2: Receive Input
    first_set_input = input()
    second_set_input = input()

    # Step 3: Split Input into Individual Numbers
    first_set = first_set_input.split()
    second_set = second_set_input.split()

    # Step 4: Initialize a Difference Counter
    difference_count = 0

    # Step 5: Compare Corresponding Numbers
    for index in range(3):  # Comparing the first three elements
        first_number = int(first_set[index])
        second_number = int(second_set[index])
        
        if first_number != second_number:
            difference_count += 1

    # Step 6: Check the Number of Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 1: Start the Program
if __name__ == "__main__":
    main()
