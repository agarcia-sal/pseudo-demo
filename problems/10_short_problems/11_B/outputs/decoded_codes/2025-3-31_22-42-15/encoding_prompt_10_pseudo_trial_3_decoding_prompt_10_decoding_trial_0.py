def main():
    # Read an integer input and calculate its absolute value
    n = abs(int(input()))
    
    i = 0  # Initialize the counter

    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2
        m = s - n  # Calculate the difference between s and n

        if s == n:
            print(i)  # Output the value of i if the sum equals n
            break  # Exit the loop
        elif s > n:
            if m % 2 == 0:  # Check if the difference is even
                print(i)  # Output the value of i if m is even
                break  # Exit the loop
        
        i += 1  # Increment i to check the next integer

if __name__ == "__main__":
    main()
