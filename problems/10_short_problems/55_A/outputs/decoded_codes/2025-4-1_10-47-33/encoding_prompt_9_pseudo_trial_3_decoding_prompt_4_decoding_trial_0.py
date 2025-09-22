def main():
    # Step 2: Receive Input
    n = int(input())  # Read an integer n from the user
    
    # Step 3: Initialize List
    status_list = [True] * n  # Create a boolean list with n elements, all initialized to True
    
    # Step 4: Initialize Variables
    current_index = 0
    increment = 1
    
    # Step 5: Process List
    while increment <= 500000:
        if status_list[current_index]:  # Check if the current index in status_list is True
            status_list[current_index] = False  # Change that element to False
        increment += 1  # Increase increment by 1
        current_index = (current_index + increment) % n  # Update the currentIndex
    
    # Step 6: Check Remaining Values
    remaining_true = [value for value in status_list if value]  # Create a list of remaining True values
    
    # Step 7: Generate Output
    if not remaining_true:  # If remaining_true is empty (i.e., all values are False)
        print("YES")
    else:
        print("NO")  # Otherwise, print "NO"

# Step 1: Start the program
if __name__ == "__main__":
    main()
