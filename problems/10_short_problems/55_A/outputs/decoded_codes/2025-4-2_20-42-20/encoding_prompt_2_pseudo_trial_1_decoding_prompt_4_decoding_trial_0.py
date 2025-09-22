def main():
    # Step 2: Get an integer input from the user
    number_of_elements = int(input())
    
    # Step 3: Create a list `isAvailable` initialized to True
    is_available = [True] * number_of_elements
    
    index = 0  # Step 4: Initialize index to 0
    increment = 1  # Step 5: Initialize increment to 1
    
    # Step 6: Loop until increment exceeds 500000
    while increment <= 500000:
        # Check if the element at `isAvailable[index]` is True
        if is_available[index]:
            # Set the element at the current index to False
            is_available[index] = False
        
        # Step 6b: Increase increment by 1
        increment += 1
        
        # Step 6c: Update index using modular arithmetic
        index = (index + increment) % number_of_elements
    
    # Step 7: Create a list of remaining True elements
    remaining_true = [value for value in is_available if value]
    
    # Step 8 & 9: Output based on the length of remainingTrue
    if len(remaining_true) == 0:
        print('YES')  # Step 8: If no elements are true
    else:
        print('NO')  # Step 9: If there are remaining true elements

# Run the main function
if __name__ == "__main__":
    main()
