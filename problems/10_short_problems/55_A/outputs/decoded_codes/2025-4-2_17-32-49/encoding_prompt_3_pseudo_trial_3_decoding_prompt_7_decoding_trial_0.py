# Begin function to execute the main logic
def main():
    # Step 1: Read input value for `n`
    n = int(input())  # Convert user input to integer

    # Step 2: Initialize a list `b` with `n` True values
    b = [True] * n  # List of size n, filled with True

    # Step 3: Set initial indices for processing
    j = 0  # Index for the list `b`
    i = 1  # Counter starting at 1
    
    # Step 4: Loop until `i` exceeds 500,000
    while i <= 500000:
        # Step 5: Check if the current position in list `b` is True
        if b[j]:  # If the value at index j is True
            # Step 6: Mark the current position in list `b` as False
            b[j] = False  # Set the value at index j to False

        # Step 7: Increment the counter `i`
        i += 1  # Increment i by 1

        # Step 8: Update the index `j` for the next iteration
        j = (j + i) % n  # Update index circularly

    # Step 9: Create a new list `x` containing only True values from `b`
    x = [value for value in b if value]  # List comprehension to filter True values

    # Step 10: Check if `x` is empty or not
    if len(x) == 0:  # If the length of x is 0
        print('YES')  # All positions are False
    else:
        print('NO')  # There are still True values present

# Call the main function to execute the code
main()
