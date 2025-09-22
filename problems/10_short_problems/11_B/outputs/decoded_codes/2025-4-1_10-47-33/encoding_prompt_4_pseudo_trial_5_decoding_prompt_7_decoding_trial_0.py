def FindTriangleNumber():
    # Read input and convert to absolute integer
    n = abs(int(input()))
    i = 0

    # Infinite loop until a valid triangle number solution is found
    while True:
        # Calculate the triangle number for the current i
        s = (i * (i + 1)) // 2  # Using integer division to find the triangle number
        m = s - n  # Determine the difference between the triangle number and input

        # Check if current triangle number equals input
        if s == n:
            print(i)  # Output the index of the triangle number
            break  # Exit loop if we found a match

        # Check if current triangle number exceeds input
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Output the index if the difference is even
                break  # Exit loop in this scenario

        # Increment to the next triangle number
        i += 1
