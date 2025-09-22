def main():
    # Step 2: Input
    n = int(input())
    
    # Step 3: Initialize list `b` with `True` values
    b = [True] * n
    
    # Step 4: Initialize `j` and `i`
    j = 0
    i = 1
    
    # Step 5: Loop while `i` is less than or equal to 500,000
    while i <= 500000:
        # Step 5.1: Check Condition
        if b[j]:
            # Mark the position as `False`
            b[j] = False
        
        # Step 5.2: Increment `i`
        i += 1
        
        # Step 5.3: Update `j`
        j = (j + i) % n
    
    # Step 6: Extract result
    x = [value for value in b if value]  # List of `True` values
    
    # Step 7: Check Length
    if len(x) == 0:
        # Step 8: Output "YES"
        print("YES")
    else:
        # Step 8: Output "NO"
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
