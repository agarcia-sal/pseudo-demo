# Function to find the smallest non-negative integer index for triangular numbers
def find_triangular_index():
    # Step 1: Read the absolute value of user input
    target_number = abs(int(input()))
    
    # Step 2: Initialize the current triangular number index
    index = 0
    
    # Step 3: Start an indefinite loop to find the required triangular number
    while True:
        # Step 4: Calculate the triangular number based on the current index
        triangular_number = (index * (index + 1)) // 2
        
        # Step 5: Find the difference between the current triangular number and the target number
        difference = triangular_number - target_number
        
        # Step 6: Check if the current triangular number is equal to the target number
        if triangular_number == target_number:
            # Step 7: Print the current index as it satisfies the condition
            print(index)
            # Step 8: Exit the loop since the solution is found
            break
        
        # Step 9: Check if the current triangular number is greater than the target number
        elif triangular_number > target_number:
            # Step 10: Check if the difference is even
            if difference % 2 == 0:
                # Step 11: Print the current index as it satisfies the condition
                print(index)
                # Step 12: Exit the loop since the solution is found
                break
        
        # Step 13: Increment the index to calculate the next triangular number in the next iteration
        index += 1

# Call the function to execute the logic
find_triangular_index()
