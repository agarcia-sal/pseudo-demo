def main():
    # Input: Get an integer from the user and convert it to its absolute value.
    number = abs(int(input()))
    
    # Initialize: Start a counter variable.
    index = 0
    
    # Loop indefinitely: Continue checking for triangular numbers.
    while True:
        # Calculate Triangular Number: Use the formula for the sum of the first index numbers.
        triangular_sum = (index * (index + 1)) // 2  # Using integer division
        
        # Calculate Difference: Determine how far the triangular number is from the input number.
        difference = triangular_sum - number
        
        # Check Conditions:
        if triangular_sum == number:
            # Print index: This indicates that number is a triangular number.
            print(index)
            break
        elif triangular_sum > number:
            if difference % 2 == 0:
                # Print index: This indicates that number can be represented as a triangular number with an adjustment.
                print(index)
                break
        
        # Increment Counter: After each iteration, increase index by 1.
        index += 1

# Execute the main function
if __name__ == "__main__":
    main()
