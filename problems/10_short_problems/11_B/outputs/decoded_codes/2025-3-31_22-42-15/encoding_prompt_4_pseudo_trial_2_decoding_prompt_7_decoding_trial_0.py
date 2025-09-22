# Import necessary library for absolute value
def main():
    # Get the absolute value of an integer from user input
    number = abs(int(input()))
    
    index = 0  # Initialize index
    
    # Infinite loop until a condition is met
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_value = (index * (index + 1)) // 2
        
        # Calculate the difference between sum and number
        difference = sum_value - number
        
        # Check if the sum equals the number
        if sum_value == number:
            print(index)  # Output index when the sum equals the number
            break
        
        # Check if the sum is greater than the number
        elif sum_value > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output index when the difference is even
                break
        
        # Increment index for the next iteration
        index += 1

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
