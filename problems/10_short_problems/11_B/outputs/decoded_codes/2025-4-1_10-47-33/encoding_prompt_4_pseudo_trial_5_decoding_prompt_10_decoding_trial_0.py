def find_triangle_number():
    # Convert input to absolute integer
    n = abs(int(input()))
    i = 0

    # Infinite loop until a solution is found
    while True:
        # Calculate the triangle number for current i
        triangle_number = (i * (i + 1)) // 2
        difference = triangle_number - n

        # Check if the current triangle number equals input
        if triangle_number == n:
            print(i)
            break
        
        # Check if the current triangle number exceeds input
        elif triangle_number > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(i)
                break

        # Increment to the next triangle number
        i += 1
