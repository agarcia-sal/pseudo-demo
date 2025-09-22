def main():
    # Step 2: Read an integer number n from user input
    n = int(input())
    
    # Step 3: Initialize the status list with n elements, all set to True
    status = [True] * n
    
    # Step 4: Initialize currentStep and index
    current_step = 1
    index = 0
    
    # Step 5: Loop while currentStep is less than or equal to 500000
    while current_step <= 500000:
        # Step 5.1: Check Status
        if status[index]:
            # Set the element to False
            status[index] = False
            
        # Step 5.2: Increment currentStep
        current_step += 1
        
        # Step 5.3: Update index
        index = (index + current_step) % n
        
    # Step 6: Filter active status
    active_elements = [elem for elem in status if elem]
    
    # Step 7: Check Result
    if len(active_elements) == 0:
        print("YES")  # No active elements
    else:
        print("NO")   # There are active elements

# Execute the main function
if __name__ == "__main__":
    main()
