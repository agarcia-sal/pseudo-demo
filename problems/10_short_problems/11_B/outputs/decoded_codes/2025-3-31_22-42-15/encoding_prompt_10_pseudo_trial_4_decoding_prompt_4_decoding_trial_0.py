def main():
    # Step 1: Initialize Variables
    n = abs(int(input()))  # Get absolute value of integer input from the user
    i = 0  # Initialize counter

    # Step 2: Start Infinite Loop
    while True:
        # Step 2a: Calculate the Sum
        s = (i * (i + 1)) // 2  # Sum of first i natural numbers using integer division

        # Step 2b: Calculate the Difference
        m = s - n  # Difference between sum s and input n

        # Step 2c: Check for Match
        if s == n:
            print(i)  # Output the index i
            break  # Exit the loop

        # Step 2d: Check for Exceeding Value
        if s > n:
            if m % 2 == 0:  # Check if the difference is even
                print(i)  # Output the index i
                break  # Exit the loop

        # Step 2e: Increment Loop Counter
        i += 1  # Move to the next natural number

# Call the main function to execute the program
if __name__ == "__main__":
    main()
