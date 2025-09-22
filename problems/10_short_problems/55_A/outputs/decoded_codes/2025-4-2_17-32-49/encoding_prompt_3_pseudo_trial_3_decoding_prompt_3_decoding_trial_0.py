def process_input():
    # Step 1: Read input value for `n`
    n = int(input())

    # Step 2: Initialize a list `b` with `n` True values
    b = [True] * n

    # Step 3: Set initial indices for processing
    j = 0
    i = 1
    
    # Step 4: Loop until `i` exceeds 500,000
    while i <= 500000:
        # Step 5: Check if the current position in list `b` is True
        if b[j]:
            # Step 6: Mark the current position in list `b` as False
            b[j] = False

        # Step 7: Increment the counter `i`
        i += 1
        
        # Step 8: Update the index `j` for the next iteration
        j = (j + i) % n  # Update index circularly

    # Step 9: Create a new list `x` containing only True values from `b`
    x = [value for value in b if value]

    # Step 10: Check if `x` is empty or not
    if len(x) == 0:
        print('YES')  # Indicating all positions are False
    else:
        print('NO')   # Indicating there are still True values present

# Example of how to call the function
process_input()
