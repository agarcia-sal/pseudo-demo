def main():
    # Step 1: Read an integer input for the size of the list.
    n = int(input())

    # Step 2: Initialize a boolean list with size n, all set to True.
    is_true = [True] * n

    # Initialize starting indices.
    j = 0
    i = 1

    # Step 3: Loop until i exceeds 500000.
    while i <= 500000:
        # If the current position in list is True.
        if is_true[j]:
            # Mark that position as False.
            is_true[j] = False

        # Increment i.
        i += 1
        
        # Update j using the formula and wrapping around with modulo.
        j = (j + i) % n 

    # Step 4: Create a list with positions in is_true that are still True.
    remaining_true_positions = [index for index, value in enumerate(is_true) if value]

    # Step 5: Check if the list is empty.
    if len(remaining_true_positions) == 0:
        print('YES')  # No True values found.
    else:
        print('NO')   # There are some True values found.

if __name__ == "__main__":
    main()
