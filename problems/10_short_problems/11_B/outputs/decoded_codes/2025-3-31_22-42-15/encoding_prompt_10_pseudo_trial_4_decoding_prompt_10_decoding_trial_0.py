def main():
    # Initialize variables
    n = abs(int(input()))  # Get absolute value of user input
    i = 0  # Loop counter

    # Start infinite loop
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Sum formula
        
        # Calculate the difference
        m = s - n

        # Check for match
        if s == n:
            print(i)  # Print the value of i
            break  # Exit the loop
        
        # Check for exceeding value
        if s > n:
            if m % 2 == 0:  # Check if m is divisible by 2
                print(i)  # Print the value of i
                break  # Exit the loop

        # Increment loop counter
        i += 1

# Entry point of the program
if __name__ == "__main__":
    main()
