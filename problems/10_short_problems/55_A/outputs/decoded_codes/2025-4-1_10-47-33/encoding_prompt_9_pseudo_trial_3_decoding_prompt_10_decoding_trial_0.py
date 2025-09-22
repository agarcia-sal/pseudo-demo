def main():
    # Step 2: Receive Input
    n = int(input())
    
    # Step 3: Initialize List
    status_list = [True] * n
    
    # Step 4: Initialize Variables
    current_index = 0
    increment = 1
    
    # Step 5: Process List
    while increment <= 500000:
        if status_list[current_index]:  # Check if current index is True
            status_list[current_index] = False  # Set it to False
        
        increment += 1  # Increase increment
        current_index = (current_index + increment) % n  # Update current index
    
    # Step 6: Check Remaining Values
    remaining_true = [status for status in status_list if status]
    
    # Step 7: Generate Output
    if not remaining_true:  # If remaining_true is empty
        print("YES")
    else:
        print("NO")

# Step 1: Start the program
if __name__ == "__main__":
    main()
