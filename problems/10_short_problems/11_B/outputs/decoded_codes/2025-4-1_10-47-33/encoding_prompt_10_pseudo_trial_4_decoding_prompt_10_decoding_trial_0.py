def find_integer(n):
    # Convert n to the absolute value
    n = abs(n)

    # Initialize i
    i = 0

    while True:
        # Calculate the sum s of the first i integers
        s = i * (i + 1) // 2
        
        # Calculate the difference m
        m = s - n

        # Check if the sum s equals n
        if s == n:
            print(i)
            break

        # Check if the sum s is greater than n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)
                break

        # Increment i for the next iteration
        i += 1

# Get user input for the integer variable n
n = int(input())
find_integer(n)
