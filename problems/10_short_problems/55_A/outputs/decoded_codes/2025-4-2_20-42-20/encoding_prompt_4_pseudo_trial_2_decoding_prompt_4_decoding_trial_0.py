def main():
    # Read an integer input for n
    n = int(input())

    # Initialize a boolean list of size n with all values set to True
    is_active = [True] * n

    # Initialize loop variables
    j = 0
    i = 1

    # Loop until i exceeds 500000
    while i <= 500000:
        # If the current element in list is_active at index j is True
        if is_active[j]:
            # Change the value at index j to False
            is_active[j] = False

        # Increment i by 1
        i += 1

        # Update j to the next index using modular arithmetic
        j = (j + i) % n

    # Create a new list of all elements from is_active that are still True
    remaining_active = [active for active in is_active if active]

    # Check if there are no True values left in the remaining_active list
    if len(remaining_active) == 0:
        print('YES')  # All positions were marked False
    else:
        print('NO')   # There are still True positions left

# Entry point of the program
if __name__ == "__main__":
    main()
