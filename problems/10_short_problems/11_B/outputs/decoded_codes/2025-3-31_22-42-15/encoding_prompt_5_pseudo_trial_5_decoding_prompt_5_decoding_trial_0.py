# Function to find the smallest non-negative integer that meets the condition with triangular numbers
def smallest_triangular_integer():
    # Get the absolute value of the input and store it as a number
    number = abs(int(input()))
    
    # Initialize a counter variable
    counter = 0
    
    # Enter an infinite loop to repeatedly check conditions
    while True:
        # Calculate the triangular number for the current counter value
        triangular_number = (counter * (counter + 1)) // 2
        
        # Calculate the difference between the triangular number and the input number
        difference = triangular_number - number
        
        # Check if the triangular number is equal to the input number
        if triangular_number == number:
            print("The result is:", counter)
            break

        # Check if the triangular number is greater than the input number
        elif triangular_number > number:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print("The result is:", counter)
                break
        
        # Increment the counter for the next iteration
        counter += 1

# Example of calling the function
# smallest_triangular_integer() # Call this in the actual implementation
