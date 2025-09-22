def find_triangle_number():
    # Input: Read a number n from user
    n = abs(int(input()))
    
    i = 0
    while True:
        # Calculate the triangular number of i
        s = (i * (i + 1)) // 2
        m = s - n
        
        if s == n:
            print(i)
            break
        elif s > n:
            if m % 2 == 0:
                print(i)
                break
        
        # Increment i by 1
        i += 1
