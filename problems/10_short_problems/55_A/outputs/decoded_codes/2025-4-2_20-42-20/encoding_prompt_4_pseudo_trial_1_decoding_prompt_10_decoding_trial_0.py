def main():
    # Step 1: Get input from the user
    n = int(input())
    
    # Step 2: Initialize a list 'b' of size 'n' with True values
    b = [True] * n
    
    j = 0
    i = 1

    # Step 3: Iterate while 'i' is less than or equal to 500000
    while i <= 500000:
        if b[j]:
            # Mark the current index 'j' as False
            b[j] = False
        # Increment 'i'
        i += 1
        # Update index 'j' for the next iteration
        j = (j + i) % n

    # Step 4: Create a list 'x' containing all values from 'b' that are True
    x = [value for value in b if value]

    # Step 5: Check the length of 'x' and print the appropriate response
    if len(x) == 0:
        print('YES')  # All elements were marked False
    else:
        print('NO')   # There are still True elements in the list

# Run the main function
if __name__ == '__main__':
    main()
