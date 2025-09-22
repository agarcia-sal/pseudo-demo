def main():
    # Step 2: Input an integer number from user
    n = int(input())
    
    # Step 3: Initialize list 'status' with all True
    status = [True] * n
    
    # Step 4: Initialize 'currentStep' and 'index'
    current_step = 1
    index = 0
    
    # Step 5: Loop until currentStep exceeds 500000
    while current_step <= 500000:
        # Step 5a: Check status at 'index'
        if status[index]:
            # Set the element to False
            status[index] = False
        
        # Step 5b: Increment currentStep by 1
        current_step += 1
        
        # Step 5c: Update index using modulo
        index = (index + current_step) % n
    
    # Step 6: Filter out active status elements
    active_elements = [s for s in status if s]
    
    # Step 7: Check the result and print accordingly
    if len(active_elements) == 0:
        print("YES")
    else:
        print("NO")

# Call the main function
if __name__ == "__main__":
    main()
