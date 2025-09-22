def main():
    # Step 1: Receive input for the number of elements in the list
    number_of_elements = int(input())
    
    # Step 2: Create a list of flags initialized to True
    flags = [True] * number_of_elements
    
    # Step 3: Initialize index and counter
    index = 0
    counter = 1
    
    # Step 4: Loop until counter is less than or equal to 500,000
    while counter <= 500000:
        # If the current flag is True, mark it as False
        if flags[index]:
            flags[index] = False
        
        # Increment counter
        counter += 1
        
        # Update index, wrap around using modulus
        index = (index + counter) % number_of_elements
    
    # Step 5: Create a list of active flags (those that are still True)
    active_flags = [flag for flag in flags if flag]
    
    # Step 6: Check the length of the active_flags list and output the result
    if not active_flags:
        print("YES")
    else:
        print("NO")

# Start the program
main()
