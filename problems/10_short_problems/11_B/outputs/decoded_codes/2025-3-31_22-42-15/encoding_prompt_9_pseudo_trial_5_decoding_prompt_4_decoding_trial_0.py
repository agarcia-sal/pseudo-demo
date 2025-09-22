def find_smallest_integer():
    # Step 1: Receive Input
    target_sum = int(input())
    
    # Step 2: Initialize Variables
    current_index = 0
    
    # Step 3: Infinite Loop
    while True:
        # Step 1 of Loop: Calculate the Sum
        current_sum = (current_index * (current_index + 1)) // 2  # Using integer division for accuracy
        
        # Step 2 of Loop: Calculate the Difference
        surplus = current_sum - target_sum
        
        # Step 3 of Loop: Check for Exact Match
        if current_sum == target_sum:
            print(current_index)
            break  # Exit the loop if the sum equals the target
        
        # Step 4 of Loop: Check for Surplus Condition
        if surplus > 0:
            if surplus % 2 == 0:  # Check if it can be evenly split
                print(current_index)
                break  # Exit the loop if surplus can be evenly divided
        
        # Step 5 of Loop: Increment Index
        current_index += 1

# Call the function to execute the program
find_smallest_integer()
