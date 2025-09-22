def main():
    # Step 1: Get an integer input from the user to determine the number of elements
    number_of_elements = int(input())
    
    # Step 2: Create a list indicating availability, initialized to True for all elements
    is_available = [True] * number_of_elements
    
    # Initialize index and increment
    index = 0
    increment = 1
    
    # Step 3: Iterate while increment is less than or equal to 500000
    while increment <= 500000:
        # Step 4: Check if the current element is available
        if is_available[index]:
            # Mark the element as not available
            is_available[index] = False
        
        # Step 5: Update increment and index
        increment += 1
        index = (index + increment) % number_of_elements
    
    # Step 6: Create a new list with remaining True values
    remaining_true = [available for available in is_available if available]
    
    # Step 7: Output 'YES' if no elements are available, otherwise output 'NO'
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

# Invoke the main function to run the program
if __name__ == "__main__":
    main()
