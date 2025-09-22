def main():
    # Step 2: Receive Input
    first_set = input()
    second_set = input()

    # Step 3: Process Input
    first_numbers = first_set.split()
    second_numbers = second_set.split()

    # Step 4: Initialize Differences Counter
    difference_count = 0

    # Step 5: Compare Numbers
    for index in range(3):  # Only compare the first three positions
        first_number = int(first_numbers[index])  # Convert to integer
        second_number = int(second_numbers[index])  # Convert to integer
        if first_number != second_number:
            difference_count += 1

    # Step 6: Determine Output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: End the program
if __name__ == "__main__":
    main()
