def main():
    # Initialize variable n as the absolute value of the integer input
    n = abs(int(input()))

    # Initialize index variable i to 0
    i = 0

    # Start an infinite loop
    while True:
        # Calculate the sum of the first i natural numbers
        sum_natural = (i * (i + 1)) // 2
        
        # Calculate the difference between sum_natural and number n
        difference = sum_natural - n
        
        # Check if the sum represents the number n
        if sum_natural == n:
            print("The value of i is:", i)
            break  # Exit the loop
                
        # Check if the sum is greater than n
        elif sum_natural > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print("The value of i is:", i)
                break  # Exit the loop
                
        # Increment the index i for the next iteration
        i += 1

if __name__ == "__main__":
    main()
