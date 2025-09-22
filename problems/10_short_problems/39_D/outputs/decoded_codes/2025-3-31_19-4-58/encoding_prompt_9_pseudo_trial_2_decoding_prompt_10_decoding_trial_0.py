def main():
    # Receive Input
    first_set = [int(input()) for _ in range(3)]
    second_set = [int(input()) for _ in range(3)]

    # Initialize Difference Count
    difference_count = 0

    # Loop through the Sets
    for index in range(3):
        if first_set[index] != second_set[index]:
            difference_count += 1

    # Check the Number of Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the program
if __name__ == "__main__":
    main()
