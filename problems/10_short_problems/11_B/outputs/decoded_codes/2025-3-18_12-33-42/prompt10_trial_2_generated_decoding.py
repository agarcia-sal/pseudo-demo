def main():
    # Get absolute value of the user input
    n = abs(int(input()))

    # Initialize a counter
    i = 0

    # Begin an indefinite loop
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between sum s and n
        m = s - n
        
        # Check if the sum s is equal to n
        if s == n:
            print(i)
            break  # Exit the loop
            
        # Check if the sum s is greater than n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)
                break  # Exit the loop
                
        # Increment the counter i for the next natural number
        i += 1

# Call the main function to execute the program
if __name__ == "__main__":
    main()
