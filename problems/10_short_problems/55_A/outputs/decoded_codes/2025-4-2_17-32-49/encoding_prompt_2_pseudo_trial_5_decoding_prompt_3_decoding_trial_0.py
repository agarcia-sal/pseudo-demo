def main():
    # Step 2: Input Requirement
    totalElements = int(input())
    
    # Step 3: Initialize
    isActive = [True] * totalElements  # List indicating the active status of elements
    index = 0  # Current position in the list
    step = 1   # Number of steps taken in each iteration
    
    # Step 4: Loop
    while step <= 500000:
        if isActive[index]:  # Check if the current element is active
            isActive[index] = False  # Mark as inactive
        
        step += 1  # Increase the step variable
        index = (index + step) % totalElements  # Update the index with wrap-around using modulo
        
    # Step 5: Filter Active Elements
    activeElements = [element for element in isActive if element]
    
    # Step 6: Output Requirement
    if len(activeElements) == 0:
        print("YES")  # All elements have been marked inactive
    else:
        print("NO")   # There are still active elements

# Call the main function to execute the code
main()
