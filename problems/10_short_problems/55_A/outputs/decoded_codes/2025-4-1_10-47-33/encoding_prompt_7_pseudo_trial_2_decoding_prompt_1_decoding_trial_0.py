def checkStatusOfElements(n):
    # INITIALIZE array 'b' of size n with all values set to True
    b = [True] * n  
    j = 0             # SET index 'j' to 0
    i = 1             # SET counter 'i' to 1
    
    # WHILE counter 'i' is less than or equal to 500000
    while i <= 500000: 
        # IF element at index 'j' in array 'b' is True
        if b[j]:  
            # SET element at index 'j' in array 'b' to False
            b[j] = False
            
        # INCREMENT counter 'i' by 1
        i += 1  
        # UPDATE index 'j' to (index 'j' + counter 'i') modulo n
        j = (j + i) % n  

    # CREATE a new array 'x' containing all True values from array 'b'
    x = [value for value in b if value]
    
    # IF length of array 'x' is 0
    if len(x) == 0:  
        print('YES')  # Indicates that all elements in 'b' have been set to False
    else:
        print('NO')   # Indicates that there are still True elements in 'b'
