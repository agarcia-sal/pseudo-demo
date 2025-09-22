def main():
    # Step 1: Receive input for the number of elements
    number_of_elements = int(input())
    
    # Step 2: Create the flags list initialized to True
    flags = [True] * number_of_elements
    
    # Step 3: Initialize index and counter
    index = 0
    counter = 1
    
    # Step 4: Iterate until counter exceeds 500,000
    while counter <= 500000:
        if flags[index]:  # Check if the current flag is True
            flags[index] = False  # Mark the flag as False
        
        # Increment counter
        counter += 1
        
        # Update index to wrap around the flags list
        index = (index + counter) % number_of_elements
    
    # Step 5: Create a list of active flags
    active_flags = [flag for flag in flags if flag]
    
    # Step 6: Output result based on the active flags list
    if len(active_flags) == 0:
        print("YES")  # All elements were marked False
    else:
        print("NO")   # Some elements remain True

# Call the main function to run the program
if __name__ == "__main__":
    main()
