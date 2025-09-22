# Function to find the smallest index whose triangular number meets the specified conditions
def find_triangular_index():
    # Obtain a positive integer from the user and store it as targetValue
    target_value = abs(int(input()))
    
    # Initialize currentIndex to 0
    current_index = 0

    # Start an infinite loop to calculate triangular numbers
    while True:
        # Calculate the triangular number for currentIndex
        triangular_number = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference between the triangular number and targetValue
        difference = triangular_number - target_value
        
        # Check if the triangular number equals the targetValue
        if triangular_number == target_value:
            print(current_index)  # Print the currentIndex
            break
        
        # Check if the triangular number is greater than the targetValue
        if triangular_number > target_value:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(current_index)  # Print the currentIndex
                break
        
        # Increment currentIndex to check the next triangular number
        current_index += 1

# To test the function, you can call find_triangular_index()
