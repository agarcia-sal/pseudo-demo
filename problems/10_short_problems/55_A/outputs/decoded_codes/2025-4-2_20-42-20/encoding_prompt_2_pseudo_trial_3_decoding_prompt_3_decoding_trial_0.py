def main():
    # Step 1: Read the number of elements from user input
    number_of_elements = int(input())
    
    # Step 2: Create a boolean list initialized to True
    boolean_list = [True] * number_of_elements
    
    # Step 3: Initialize position and increment variables
    position = 0
    increment = 1
    
    # Step 4: Repeat the process while increment is less than or equal to 500,000
    while increment <= 500000:
        # Step 5: Check the current entry at index position
        if boolean_list[position]:
            # If it's True, set it to False
            boolean_list[position] = False
        
        # Increase the increment
        increment += 1
        
        # Update position with wrap around using modulus operation
        position = (position + increment) % number_of_elements
    
    # Step 6: Filter the remaining True values from the boolean list
    remaining_true_values = [value for value in boolean_list if value]
    
    # Step 7: Output results based on the length of remaining true values
    if len(remaining_true_values) == 0:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
