def main():
    # Step 1: Read an integer input for n
    n = int(input())

    # Step 2: Initialize a boolean list of size n with all values set to True
    is_true_list = [True] * n

    # Step 3: Initialize variables j and i
    j = 0
    i = 1

    # Step 4: Loop until i exceeds 500000
    while i <= 500000:
        # If the current element in list is True
        if is_true_list[j]:
            # Change the value at index j to False
            is_true_list[j] = False

        # Increment i by 1
        i += 1
        
        # Update j to the next index using modular arithmetic
        j = (j + i) % n

    # Step 5: Create a new list containing all elements from is_true_list that are still True
    true_positions = [value for value in is_true_list if value]

    # Step 6: Check if there are no True values left in true_positions
    if len(true_positions) == 0:
        print('YES')  # All positions were marked False
    else:
        print('NO')   # There are still True positions left

# Entry point of the Python program
if __name__ == "__main__":
    main()
