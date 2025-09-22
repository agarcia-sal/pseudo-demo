# Function to find the smallest non-negative index whose triangular number
# meets or exceeds the given target value, and checks the difference for evenness.
def find_triangular_index():
    # Step 1: Obtain a positive integer from the user
    target_value = abs(int(input()))
    
    # Step 2: Initialize 'currentIndex' to 0
    current_index = 0
    
    while True:  # Step 3: Begin an infinite loop
        # Step 3a: Calculate the triangular number
        triangular_number = (current_index * (current_index + 1)) // 2
        
        # Step 3b: Calculate the difference
        difference = triangular_number - target_value
        
        # Step 3c: Check if it equals the targetValue
        if triangular_number == target_value:
            print(current_index)  # Print the currentIndex
            break
        
        # Step 3d: Check if triangular number is greater than targetValue
        if triangular_number > target_value:
            # Step 3d: Check if the difference is even
            if difference % 2 == 0:
                print(current_index)  # Print the currentIndex
                break
        
        current_index += 1  # Step 3e: Increment 'currentIndex'

# Execute the function
find_triangular_index()
