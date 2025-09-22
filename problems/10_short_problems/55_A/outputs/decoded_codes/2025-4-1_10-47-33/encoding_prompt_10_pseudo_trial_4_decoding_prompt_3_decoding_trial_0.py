def main():
    # Step 1: Input Handling
    n = int(input())
    
    # Step 2: Initialize a boolean list b
    b = [True] * n  # A list of boolean values initialized to True
    j = 0
    i = 1

    # Step 3: Loop to modify the boolean list
    while i <= 500000:
        if b[j]:  # If b[j] is True
            b[j] = False  # Mark it as False
        
        # Step 4: Increment i and update j
        i += 1
        j = (j + i) % n  # Update index j

    # Step 5: Extract remaining TRUE values from b
    remaining_true_values = [value for value in b if value]  # Get elements that are still True

    # Step 6: Check the result and print output
    if len(remaining_true_values) == 0:
        print('YES')
    else:
        print('NO')

# Call the main function to run the code
if __name__ == "__main__":
    main()
