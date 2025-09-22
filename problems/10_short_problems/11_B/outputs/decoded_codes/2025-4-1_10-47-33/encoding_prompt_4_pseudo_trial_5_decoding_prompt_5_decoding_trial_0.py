def find_triangle_number():
    # Get user input and convert it to an absolute integer
    n = abs(int(input()))
    i = 0

    # Infinite loop until a solution is found
    while True:
        # Calculate the triangle number for the current i
        triangle_number = (i * (i + 1)) // 2
        difference = triangle_number - n

        # Check if the current triangle number equals the input
        if triangle_number == n:
            print(i)
            break

        # Check if the current triangle number exceeds the input
        elif triangle_number > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(i)
                break

        # Increment to the next triangle number
        i += 1

# Example test case (you can uncomment to test)
# This would wait for input; for testing, you can provide input as a prompt.
# find_triangle_number()
