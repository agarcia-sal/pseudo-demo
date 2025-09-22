def find_triangle_number():
    # Step 2: Input
    n = int(input())  # Read a number n from user
    n = abs(n)  # n = absolute value of n
    
    i = 0  # SET i = 0
    while True:  # WHILE TRUE:
        s = (i * (i + 1)) // 2  # s = triangular number of i
        m = s - n  # m = s - n
        
        if s == n:  # IF s equals n THEN
            print(i)  # PRINT i
            break  # BREAK
        
        elif s > n:  # ELSE IF s greater than n THEN
            if m % 2 == 0:  # IF m is even THEN
                print(i)  # PRINT i
                break  # BREAK
            
        i += 1  # INCREMENT i by 1
