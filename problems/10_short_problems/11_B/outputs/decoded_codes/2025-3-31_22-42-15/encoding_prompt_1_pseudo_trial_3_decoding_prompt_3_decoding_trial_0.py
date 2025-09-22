def find_triangle_index():
    # Step 2: Receive Input
    targetValue = abs(int(input()))
    
    # Step 3: Initialize Counter
    index = 0
    
    # Step 4: Infinite Loop
    while True:
        # Step 4a: Calculate Triangle Number
        triangularNumber = (index * (index + 1)) // 2
        
        # Step 4b: Calculate Difference
        difference = triangularNumber - targetValue
        
        # Step 4c: Check Conditions
        if triangularNumber == targetValue:
            print(index)
            break
        elif triangularNumber > targetValue:
            if difference % 2 == 0:
                print(index)
                break
                
        # Step 4d: Increment Counter
        index += 1

# Execute the function
find_triangle_index()
