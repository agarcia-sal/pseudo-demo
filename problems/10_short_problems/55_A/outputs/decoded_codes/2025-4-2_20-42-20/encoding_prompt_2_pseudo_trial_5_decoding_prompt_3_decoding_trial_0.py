def process_boolean_array():
    # Step 1: Read an integer input representing totalCount
    total_count = int(input())
    
    # Step 2: Create a boolean array of size totalCount, all initialized to True
    boolean_array = [True] * total_count
    
    # Step 3: Initialize incrementValue and index
    increment_value = 1
    index = 0
    
    # Step 4: Start the loop that continues while incrementValue <= 500000
    while increment_value <= 500000:
        # If the current position in boolean_array is True
        if boolean_array[index]:
            # Set that position to False
            boolean_array[index] = False
        
        # Next iteration preparation
        increment_value += 1
        index = (index + increment_value) % total_count  # Wrap around using modulus
    
    # Step 5: Create the trueValues list containing positions still True
    true_values = [index for index, value in enumerate(boolean_array) if value]
    
    # Step 6: Check the size of trueValues and print the result
    if len(true_values) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
process_boolean_array()
