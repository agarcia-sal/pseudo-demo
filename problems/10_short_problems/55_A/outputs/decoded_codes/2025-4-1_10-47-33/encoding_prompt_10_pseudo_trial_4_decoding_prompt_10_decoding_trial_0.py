def main():
    # Step 1: Input Handling
    n = int(input())
    
    # Step 2: Initialize a boolean list with all values set to True
    boolean_list = [True] * n
    j = 0
    i = 1

    # Step 3: Loop to modify the boolean list
    while i <= 500000:
        if boolean_list[j]:  # Check if the current index is True
            boolean_list[j] = False  # Set it to False
        
        # Step 4: Increment i and update j
        i += 1
        j = (j + i) % n  # Update j with wrap-around using modulus
    
    # Step 5: Extract remaining True values into a new list
    remaining_true_values = [value for value in boolean_list if value]

    # Step 6: Check the result and print output
    if len(remaining_true_values) == 0:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
