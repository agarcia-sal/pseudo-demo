def main():
    # Step 1: Set up input
    n = int(input())  # Read an integer n from user input

    # Step 2: Initialize a list
    is_not_deleted = [True] * n  # Create a list of size n with all elements set to True

    # Step 3: Set initial variables
    current_index = 0
    i = 1

    # Step 4: Loop through a range
    while i <= 500000:
        if is_not_deleted[current_index]:  # Check if the current index is not deleted
            is_not_deleted[current_index] = False  # Mark as deleted
        i += 1  # Increment i by 1
        current_index = (current_index + i) % n  # Update current index with wrap around logic

    # Step 5: Check for remaining True values
    remaining_true = [val for val in is_not_deleted if val]  # List of all elements still True

    # Step 6: Determine output based on remaining values
    if len(remaining_true) == 0:  # If no True values left
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
