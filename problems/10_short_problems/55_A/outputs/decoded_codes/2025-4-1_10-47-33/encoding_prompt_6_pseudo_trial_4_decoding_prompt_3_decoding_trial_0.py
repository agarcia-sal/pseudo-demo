def main():
    # Step 1: Read an integer input n
    number_of_elements = int(input())  # Read integer input

    # Step 2: Create a list 'is_active' of boolean values, initially all set to True
    is_active = [True] * number_of_elements

    # Step 3: Initialize the index variables
    current_index = 0
    increment = 1

    # Step 4: Loop until increment reaches or exceeds 500000
    while increment <= 500000:
        
        # Step 5: If the current position in 'is_active' is True
        if is_active[current_index]:
            # Step 6: Set the current position in 'is_active' to False
            is_active[current_index] = False
        
        # Step 7: Increment the increment value
        increment += 1
        
        # Step 8: Update current_index using modular arithmetic
        current_index = (current_index + increment) % number_of_elements
     
    # Step 9: Create a new list 'active_elements' with True values from 'is_active'
    active_elements = [state for state in is_active if state]

    # Step 10: Check if 'active_elements' is empty
    if len(active_elements) == 0:
        # Step 11: If empty, output 'YES'
        print('YES')
    else:
        # Step 12: If not empty, output 'NO'
        print('NO')

# Call the main function to execute the code
main()
