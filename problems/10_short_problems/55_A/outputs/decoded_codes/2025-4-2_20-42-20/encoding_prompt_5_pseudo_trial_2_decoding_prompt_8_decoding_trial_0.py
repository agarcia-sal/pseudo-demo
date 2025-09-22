def main():
    # Step 2: Retrieve Input
    n = int(input())
    
    # Step 3: Initialize List
    status = [True] * n
    
    # Step 4: Initialize Variables
    index = 0
    increment = 1
    
    # Step 5: Perform Modifications
    while increment <= 500000:
        if status[index]:  # Check if current element is active
            status[index] = False  # Mark it as inactive
        
        increment += 1  # Increase increment
        index = (index + increment) % n  # Update index wrapping around the list
    
    # Step 6: Check Remaining Active Elements
    active_elements = [s for s in status if s]  # Get all true values
    
    # Step 7: Determine Output
    if len(active_elements) == 0:  # If no elements are active
        print("YES")
    else:
        print("NO")

# Step 1: Start Program
main()
