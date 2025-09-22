def main():
    # Step 1: Input Handling
    n = int(input())
    
    # Step 2: Initialize a boolean list b
    b = [True] * n  # Creates a list of size n with all values set to True
    j = 0
    i = 1

    # Step 3: Loop to modify the boolean list
    while i <= 500000:
        if b[j]:  # Check if the current index is True
            b[j] = False  # Set the current index to False
        
        # Step 4: Increment i and update j
        i += 1
        j = (j + i) % n  # Update j using the new value of i

    # Step 5: Extract remaining TRUE values from b
    remaining_true = [value for value in b if value]  # List comprehension to filter True values

    # Step 6: Check the result and print output
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

# Call the main function
if __name__ == "__main__":
    main()


    1
    

    2
    

    10
    

    0
    