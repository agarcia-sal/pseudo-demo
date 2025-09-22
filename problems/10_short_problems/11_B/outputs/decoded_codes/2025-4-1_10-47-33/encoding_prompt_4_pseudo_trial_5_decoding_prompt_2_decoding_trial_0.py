def FindTriangleNumber():
    # Convert input to absolute integer
    n = abs(int(input()))
    i = 0

    # Infinite loop until a solution is found
    while True:
        # Calculate the triangle number for current i
        s = (i * (i + 1)) // 2
        m = s - n

        # Check if current triangle number equals input
        if s == n:
            print(i)
            break

        # Check if current triangle number exceeds input
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)
                break

        # Increment to the next triangle number
        i += 1
