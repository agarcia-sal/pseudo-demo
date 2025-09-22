# Function to check if there are any active elements in the list after processing
def check_active_elements():
    # Get the number of elements from user input
    n = int(input())
    
    # Initialize the list to track active elements, all set to True initially
    isActive = [True] * n
    
    # Initialize index and step variables
    currentIndex = 0
    step = 1
    
    # Process the list until the step exceeds 500,000
    while step <= 500000:
        # Check if the current element is still active
        if isActive[currentIndex]:
            # Deactivate the element
            isActive[currentIndex] = False
        
        # Update the step for the next iteration
        step += 1
        
        # Calculate the new index, wrapping around the list size
        currentIndex = (currentIndex + step) % n
    
    # Filter the list to find remaining active elements
    remainingActive = [active for active in isActive if active]
    
    # Output the result based on remaining active elements
    if len(remainingActive) == 0:
        print("YES")
    else:
        print("NO")

# Example test case
# Uncomment the following line to run the function
# check_active_elements()
