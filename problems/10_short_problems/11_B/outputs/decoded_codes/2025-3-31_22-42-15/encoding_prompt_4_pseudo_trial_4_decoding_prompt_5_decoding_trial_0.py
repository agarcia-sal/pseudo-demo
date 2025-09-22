def find_solution():
    # Prompt user for input and store the absolute value of the integer
    number = abs(int(input()))
    
    # Initialize a counter variable
    index = 0
    
    # Infinite loop to find the solution
    while True:
        # Calculate the sum of the first 'index' integers
        total_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the input number
        difference = total_sum - number
        
        # Check if the sum equals the input number
        if total_sum == number:
            print(index)  # Output the index
            break  # Exit the loop
            
        # Check if the sum exceeds the input number
        elif total_sum > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break  # Exit the loop
        
        # Increment the counter variable
        index += 1

# Uncomment the following line to run the function
# find_solution()

# Test cases can be added below
# Example test cases:
# Input: 3 (should output 2)
# Input: 5 (should output 5)
# Input: 4 (should output 3)
