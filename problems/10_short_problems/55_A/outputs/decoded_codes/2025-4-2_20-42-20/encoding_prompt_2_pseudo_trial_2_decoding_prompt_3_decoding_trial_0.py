def main():
    # Step 1: Receive an integer input
    number_of_elements = int(input())
    
    # Step 2: Create the flags list initialized to True
    flags = [True] * number_of_elements
    
    # Step 3: Initialize index and counter
    index = 0
    counter = 1
    
    # Step 4: Loop controlling the iterations
    while counter <= 500000:
        # If the current entry in flags is True
        if flags[index]:
            flags[index] = False  # Mark the current entry as False
        
        counter += 1  # Increment the counter
        index = (index + counter) % number_of_elements  # Update index with wrapping
    
    # Step 5: Create a list of active flags
    active_flags = [flag for flag in flags if flag]  # Include only True entries
    
    # Step 6: Check the length of active_flags and print the result
    if not active_flags:  # If active_flags is empty
        print("YES")
    else:
        print("NO")

# Ensure the main function is called to execute the program
if __name__ == "__main__":
    main()
