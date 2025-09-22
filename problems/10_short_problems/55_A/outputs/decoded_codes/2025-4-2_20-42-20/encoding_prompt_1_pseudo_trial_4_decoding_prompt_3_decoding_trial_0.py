def main():
    # Step 2: Read an integer value `n` which represents the number of elements.
    n = int(input())
    
    # Step 3: Create a list `b` of size `n`, initialized to `True`.
    b = [True] * n
    
    # Step 4: Initialize `j` to 0 and `i` to 1.
    j = 0
    i = 1
    
    # Step 5: Loop while `i` is less than or equal to 500,000.
    while i <= 500000:
        # Step 5a: Check if position `j` in list `b` is True.
        if b[j]:
            # Step 5b: Mark this position as False.
            b[j] = False
            
        # Step 5c: Increment `i` by 1.
        i += 1
        
        # Step 5d: Update `j` to the next position, wrapping around if necessary.
        j = (j + i) % n
    
    # Step 6: Extract `x`, a list of all `True` values from list `b`.
    x = [value for value in b if value]
    
    # Step 7: Check length of `x`, and print output accordingly.
    if len(x) == 0:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program.
main()
