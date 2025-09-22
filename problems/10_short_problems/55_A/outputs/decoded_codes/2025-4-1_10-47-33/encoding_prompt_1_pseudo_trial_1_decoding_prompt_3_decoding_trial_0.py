def process_inclusion():
    # Step 1: Initialize the variable with user input as an integer
    number_of_elements = int(input())
    
    # Step 2: Create a list of boolean values initialized to True
    is_included = [True] * number_of_elements
    
    # Step 3: Initialize current index and increment
    current_index = 0
    increment = 1
    
    # Step 5: Iterate while increment is less than or equal to 500,000
    while increment <= 500000:
        # If the current index's value is True, set it to False
        if is_included[current_index]:
            is_included[current_index] = False
            
        # Increment and update current index
        increment += 1
        current_index = (current_index + increment) % number_of_elements

    # Step 6: Create a list of True values from the is_included list
    true_values = [value for value in is_included if value]
    
    # Step 7: Check the length of trueValues and print the appropriate output
    if len(true_values) == 0:
        print("YES")
    else:
        print("NO")
