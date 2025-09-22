def main():
    # Read an integer input and convert it to its absolute value
    input_number = abs(int(input()))
    
    # Initialize a variable to keep track of the current index
    current_index = 0
    
    # Infinite loop to evaluate conditions
    while True:
        # Calculate the sum of the first 'current_index' natural numbers
        sum_natural_numbers = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference between the 'sum' and the input number
        difference = sum_natural_numbers - input_number
        
        # Check if the calculated sum equals the input number
        if sum_natural_numbers == input_number:
            print(current_index)  # Print the current index
            break  # Exit the loop
        
        # Check if the calculated sum exceeds the input number
        elif sum_natural_numbers > input_number:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(current_index)  # Print the current index
                break  # Exit the loop
        
        # Increment the current index for the next iteration
        current_index += 1

if __name__ == "__main__":
    main()
