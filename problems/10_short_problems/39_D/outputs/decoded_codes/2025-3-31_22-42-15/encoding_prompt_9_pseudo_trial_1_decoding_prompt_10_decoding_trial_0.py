def main():
    # Step 2: Receive Input
    first_set = input()
    second_set = input()

    # Step 3: Split Input into Individual Numbers
    first_numbers = first_set.split()
    second_numbers = second_set.split()

    # Step 4: Initialize Difference Count
    difference_count = 0

    # Step 5: Compare the Numbers
    for i in range(3):  # We know there are exactly three numbers
        first_number = int(first_numbers[i])  # Convert first number to integer
        second_number = int(second_numbers[i])  # Convert second number to integer

        if first_number != second_number:  # If numbers differ
            difference_count += 1  # Increment difference count

    # Step 6: Evaluate Differences
    if difference_count < 3:
        print("YES")  # Output if differing in less than 3 positions
    else:
        print("NO")   # Output if differing in 3 or more positions

# Entry point for the program
if __name__ == "__main__":
    main()
