def find_smallest_integer():
    # Step 1: Receive Input
    target_value = abs(int(input()))
    
    # Step 2: Initialize Variables
    index = 0
    
    # Step 3: Infinite Loop
    while True:
        # Step 1.1: Calculate the current sum
        current_sum = (index * (index + 1)) // 2  # Using integer division for exact result
        
        # Step 1.2: Calculate the difference
        diff = current_sum - target_value
        
        # Step 1.3: Check for equality
        if current_sum == target_value:
            print(index)
            break
        
        # Step 1.4: Check for greater sum
        if current_sum > target_value:
            if diff % 2 == 0:  # Check if diff is even
                print(index)
                break
        
        # Step 1.5: Increment index
        index += 1

# Call the function to execute the program
find_smallest_integer()
