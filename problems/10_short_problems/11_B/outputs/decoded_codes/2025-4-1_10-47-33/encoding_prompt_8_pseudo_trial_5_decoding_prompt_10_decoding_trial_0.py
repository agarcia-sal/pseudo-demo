def main():
    # Step 1: Capture user input and convert it to a non-negative integer
    input_value = abs(int(input()))
    
    # Step 2: Initialize a counter
    current_index = 0
    
    # Step 3: Create an infinite loop for calculations
    while True:
        # Step 3a: Calculate the triangular number
        triangular_sum = (current_index * (current_index + 1)) // 2
        
        # Step 3b: Determine the difference
        difference = triangular_sum - input_value
        
        # Step 3c: Check for exact match
        if triangular_sum == input_value:
            print(current_index)
            break
            
        # Step 3d: Check for condition when triangular sum exceeds input value
        if triangular_sum > input_value:
            if difference % 2 == 0:  # Check if difference is even
                print(current_index)
                break
        
        # Step 3e: Increment the counter
        current_index += 1
    
# Step 4: Call the main function to execute the program
if __name__ == "__main__":
    main()
