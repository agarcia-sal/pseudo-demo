def process_boolean_array():
    # Step 1: Read an integer input which represents the total number of elements in the array
    total_count = int(input())
    
    # Step 2: Create an array booleanArray initialized to True
    boolean_array = [True] * total_count
    
    # Step 3: Initialize control variables
    increment_value = 1
    index = 0
    
    # Step 4: Continue the loop until incrementValue exceeds 500,000
    while increment_value <= 500000:
        # Check if the current position in booleanArray holds a value of True
        if boolean_array[index]:
            # Change the value at the current index to False
            boolean_array[index] = False
        
        # Increase incrementValue by 1
        increment_value += 1
        
        # Update index using modulus to wrap around
        index = (index + increment_value) % total_count
    
    # Step 5: Create a new list containing all indices where booleanArray is still True
    true_values = [i for i, val in enumerate(boolean_array) if val]

    # Step 6: Check the size of trueValues and print the result
    if not true_values:
        print("YES")
    else:
        print("NO")

# Example usage
process_boolean_array()
