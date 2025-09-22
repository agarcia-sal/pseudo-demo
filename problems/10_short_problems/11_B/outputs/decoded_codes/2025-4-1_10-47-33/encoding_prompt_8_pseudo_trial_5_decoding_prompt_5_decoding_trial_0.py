# Function to find a non-negative integer based on triangular number conditions
def find_triangular_number():
    # Capture user input and convert to a non-negative integer
    inputValue = abs(int(input()))
    
    # Initialize a counter for the triangular number calculation
    currentIndex = 0

    # Infinite loop for calculating triangular numbers
    while True:
        # Calculate the triangular number for the current index
        triangularSum = (currentIndex * (currentIndex + 1)) // 2
        
        # Calculate the difference between triangularSum and inputValue
        difference = triangularSum - inputValue
        
        # Check if we found an exact match
        if triangularSum == inputValue:
            print(currentIndex)  # Output the result
            break  # Exit the loop
        
        # Check when triangularSum exceeds inputValue
        if triangularSum > inputValue:
            # Check if the difference is even
            if difference % 2 == 0:
                print(currentIndex)  # Output the result
                break  # Exit the loop
        
        # Increment the counter to check the next triangular number
        currentIndex += 1

# Call the function to execute the program
find_triangular_number()
