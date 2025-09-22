def main():
    # Step 1: Get the size of the list from user input
    n = int(input())
    
    # Step 2: Initialize a list with n elements all set to True
    boolean_list = [True] * n

    # Step 3: Initialize counters
    outer_counter = 1
    inner_counter = 0

    # Step 4: Elimination Loop
    while outer_counter <= 500000:
        # Eliminate the current element if it's True
        if boolean_list[inner_counter]:
            boolean_list[inner_counter] = False  # Mark as eliminated
        
        # Update counters
        outer_counter += 1
        inner_counter = (inner_counter + outer_counter) % n

    # Step 5: Check remaining True values
    remaining_true_values = [value for value in boolean_list if value]

    # Step 6: Determine the result
    if len(remaining_true_values) == 0:
        print('YES')  # All values eliminated
    else:
        print('NO')   # Some values are still True

# Entry point for the program
if __name__ == "__main__":
    main()
