def main():
    # Step 1: Input and Setup
    n = int(input())  # Prompt user for input n
    b = [True] * n    # Initialize b as an array of True
    j = 0
    i = 1

    # Step 2: Iterate while i is less than or equal to 500000
    while i <= 500000:
        # Step 3: Check the value of b at index j
        if b[j]:
            b[j] = False  # Mark this index as False

        # Step 4: Update indices
        i += 1
        j = (j + i) % n  # Wrap around using modulus operator

    # Step 5: Filter TRUE values from array b
    x = [value for value in b if value]  # Get all True values in b

    # Step 6: Check if array x is empty
    if len(x) == 0:
        print('YES')  # No True values found
    else:
        print('NO')   # There are True values found

if __name__ == "__main__":
    main()
