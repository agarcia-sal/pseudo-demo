# Start of the program
def main():
    # Read an integer from the user and ensure it's non-negative
    n = abs(int(input()))  # Convert input to integer and take absolute value
    i = 0
    
    # Infinite loop to calculate and check conditions
    while True:
        # Calculate the sum of the first i natural numbers (triangular number)
        triangular_sum = (i * (i + 1)) // 2
        
        # Calculate the difference between the sum and n
        difference = triangular_sum - n
        
        # Check if the current sum equals n
        if triangular_sum == n:
            print(i)
            break
        
        # Check if the current sum exceeds n
        elif triangular_sum > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(i)
                break
        
        # Increment i for the next iteration
        i += 1

# Execute the main function
if __name__ == "__main__":
    main()
