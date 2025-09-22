def main():
    # Step 2: Read the number of elements from user input
    number_of_elements = int(input())
    
    # Step 3: Initialize a list of boolean values, all set to True
    boolean_list = [True] * number_of_elements
    
    # Step 4: Initialize variables for position and increment
    position = 0
    increment = 1
    
    # Step 5: Begin the loop while increment is less than or equal to 500,000
    while increment <= 500000:
        # Step 5a: Check if the current entry is True
        if boolean_list[position]:
            # If it is True, set it to False
            boolean_list[position] = False
        
        # Step 5b: Increase increment by 1
        increment += 1
        
        # Step 5c: Update the position
        position = (position + increment) % number_of_elements
    
    # Step 6: Create a list of remaining True values
    remaining_true_values = [value for value in boolean_list if value]
    
    # Step 7: Check if there are no remaining True values
    if len(remaining_true_values) == 0:
        print('YES')  # Step 7a: Output 'YES' if none remain
    else:
        print('NO')   # Step 8a: Output 'NO' otherwise

# Execute the main function
if __name__ == "__main__":
    main()
