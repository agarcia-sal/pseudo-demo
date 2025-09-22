def find_triangle_number():
    # Read a number from the user
    n = int(input())
    
    # Take the absolute value of n
    n = abs(n)

    i = 0
    # Infinite loop to calculate triangular numbers
    while True:
        # Calculate the triangular number for index i
        s = (i * (i + 1)) // 2
        m = s - n
        
        # Check if the triangular number equals n
        if s == n:
            print(i)
            break

        # Check if the triangular number exceeds n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)
                break
        
        # Increment the index i
        i += 1
