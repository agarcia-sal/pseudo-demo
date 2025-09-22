def check_elements():
    # Step 1: Input the integer value representing the number of elements (n).
    n = int(input())
    
    # Step 2: Initialize a list (b) of size n with all values set to True.
    b = [True] * n
    
    # Step 3: Set index variable j to 0.
    j = 0
    
    # Step 4: Set counter variable i to 1.
    i = 1
    
    # Step 5: While i is less than or equal to 500000
    while i <= 500000:
        # Step 5.1: If the value at index j in list b is True
        if b[j]:
            # Step 5.2: Set the value at index j in list b to False.
            b[j] = False
        
        # Increment counter variable i by 1.
        i += 1
        
        # Update index j to be (j + i) % n.
        j = (j + i) % n
    
    # Step 6: Create a new list (x) containing all True values from list b.
    x = [value for value in b if value]
    
    # Step 7: Check the length of list x
    if len(x) == 0:
        # Step 7.1: Output "YES".
        print("YES")
    else:
        # Step 8: Output "NO".
        print("NO")

# Example of how to call the function to run the program.
check_elements()
