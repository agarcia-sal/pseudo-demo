def main():
    # Step 1: Get an integer input from the user for number of elements
    number_of_elements = int(input())
    
    # Step 2: Create a list initialized to True
    is_available = [True] * number_of_elements
    
    # Initialize variables
    index = 0
    increment = 1
    
    # Step 6: While increment is less than or equal to 500000
    while increment <= 500000:
        # Check if the current element is True
        if is_available[index]:
            # Set the current element to False
            is_available[index] = False
            
        # Increase increment
        increment += 1
        
        # Update index using modulo operation
        index = (index + increment) % number_of_elements
    
    # Step 7: Create a list of remaining True elements
    remaining_true = [value for value in is_available if value]
    
    # Step 8: Check if length of remainingTrue is zero
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
