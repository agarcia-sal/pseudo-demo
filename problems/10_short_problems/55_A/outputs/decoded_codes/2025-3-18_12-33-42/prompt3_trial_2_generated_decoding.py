def process_elements():
    # Step 1: Read the input
    number_of_elements = int(input())
    
    # Step 2: Initialize a boolean list with size number_of_elements
    boolean_list = [True] * number_of_elements
    
    # Step 3: Initialize parameters for indexing and iteration
    index = 0
    increment = 1
    
    # Step 4: Iterate until increment is less than or equal to 500000
    while increment <= 500000:
        # Step 5: Check the value at the current index in the boolean list
        if boolean_list[index]:
            boolean_list[index] = False  # Mark this index as processed
            
        # Step 6: Update increment value and calculate the new index
        increment += 1
        index = (index + increment) % number_of_elements  # Wrap around using modulo
    
    # Step 7: Filter the boolean list to find all TRUE values
    filtered_list = [value for value in boolean_list if value]
    
    # Step 8: Check the length of the filtered list
    if len(filtered_list) == 0:
        print("YES")  # No TRUE values found
    else:
        print("NO")   # There are TRUE values found

# Calling the function to execute
process_elements()
