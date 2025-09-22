def main():
    # Read input and convert to absolute integer
    n = abs(int(input()))

    # Initialize counter
    i = 0

    # Infinite loop to search for the solution
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2

        # Calculate the difference between the sum and n
        m = s - n

        # Check if the sum equals n
        if s == n:
            print(i)
            break

        # Check if the sum exceeds n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)
                break
        
        # Increment counter for the next iteration
        i += 1

if __name__ == "__main__":
    main()
