def main():
    # Step 1: Initialize variables
    n = int(input())  # User input for size of list b
    b = [True] * n    # List b of size n initialized with True
    j = 0              # Initialize j to 0
    i = 1              # Initialize i to 1

    # Step 2: Iterate while i is less than or equal to 500000
    while i <= 500000:
        # Step 3: Check if the current position j in list b is True
        if b[j]:
            b[j] = False  # Mark the current position as False

        # Step 4: Update the variables for the next iteration
        i += 1
        j = (j + i) % n  # Wrap around the index using modulo operation

    # Step 5: Filter the list to find remaining True values
    x = [value for value in b if value]  # Create a new list x with True values

    # Step 6: Check the length of the filtered list x
    if len(x) == 0:
        print('YES')  # No True values found
    else:
        print('NO')   # Some True values found

# Entry point of the program
if __name__ == "__main__":
    main()
