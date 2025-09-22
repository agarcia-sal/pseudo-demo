def main():
    # Step 1: Get user input as an integer
    n = int(input())
    
    # Step 2: Create a list b of size n, initialized with True
    b = [True] * n
    
    # Initialize indices j and i
    j = 0
    i = 1
    
    # Step 3: Loop while i is less than or equal to 500000
    while i <= 500000:
        # If the current index j in list b is True
        if b[j]:
            # Set the value at index j in list b to False
            b[j] = False
        
        # Increment i by 1
        i += 1
        
        # Update j to the next position based on the new value of i, wrapping around with modulo
        j = (j + i) % n
    
    # Step 4: Create a list x containing all True values from list b
    x = [value for value in b if value]
    
    # Step 5: Check if list x is empty and print 'YES' or 'NO'
    print('YES' if not x else 'NO')

# Entry point for the script
if __name__ == "__main__":
    main()
