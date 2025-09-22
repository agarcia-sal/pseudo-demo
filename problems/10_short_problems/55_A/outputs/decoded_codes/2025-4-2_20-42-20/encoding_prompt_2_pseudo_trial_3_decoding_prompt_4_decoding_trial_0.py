def main():
    # Step 2: Declare an integer variable 'number_of_elements' and read its value from user input.
    number_of_elements = int(input())
    
    # Step 3: Create a list called 'boolean_list' with 'number_of_elements' entries, all set to True.
    boolean_list = [True] * number_of_elements
    
    # Step 4: Initialize two integer variables: 'position' set to 0 and 'increment' set to 1.
    position = 0
    increment = 1
    
    # Step 5: Repeat the following steps while 'increment' is less than or equal to 500,000:
    while increment <= 500000:
        # Step 5a: Check if the current entry in 'boolean_list' at index 'position' is True.
        if boolean_list[position]:
            # If it is True, set that entry to False.
            boolean_list[position] = False
        
        # Step 5b: Increase 'increment' by 1.
        increment += 1
        
        # Step 5c: Update 'position' to be the current 'position' plus 'increment'.
        # Use modulus operation to ensure 'position' stays within the bounds of 'number_of_elements'.
        position = (position + increment) % number_of_elements
    
    # Step 6: Create a new list called 'remaining_true_values' which contains all entries from 'boolean_list' that are still True.
    remaining_true_values = [value for value in boolean_list if value]
    
    # Step 7: If the length of 'remaining_true_values' is equal to 0:
    if len(remaining_true_values) == 0:
        # Step 7a: Output 'YES'.
        print('YES')
    else:
        # Step 8a: Output 'NO'.
        print('NO')

# Step 1: Start the program.
if __name__ == "__main__":
    main()
