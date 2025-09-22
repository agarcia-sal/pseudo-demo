def main():
    # Step 1: Read an integer value 'n' from input
    n = int(input())
    
    # Step 2: Initialize a list 'b' of size 'n' with all elements set to True
    b = [True] * n 
    
    # Step 3: Initialize two variables 'j' and 'i'
    j = 0
    i = 1
    
    # Step 4: Loop until 'i' exceeds 500000
    while i <= 500000:
        # Step 5: If the current position 'j' in list 'b' is True
        if b[j]:
            # Mark the position 'j' as False
            b[j] = False
        
        # Increment 'i' by 1
        i += 1
        
        # Update 'j' as the new index using the formula
        j = (j + i) % n
    
    # Step 6: Create a list 'x' of all True values remaining in 'b'
    x = [value for value in b if value]
    
    # Step 7: Check if the list 'x' is empty
    if len(x) == 0:
        # Print 'YES' if no True values are found
        print('YES')
    else:
        # Print 'NO' if there are remaining True values
        print('NO')

# Execute the main function
if __name__ == "__main__":
    main()
