# Check Values in a List

def check_active_values():
    # Step 2: Read an integer value n from user input
    n = int(input())
    
    # Step 3: Create a list isActive of length n, initialized to True
    is_active = [True] * n
    
    # Step 4: Initialize currentIndex and increment
    current_index = 0
    increment = 1
    
    # Step 6: While increment is less than or equal to 500000
    while increment <= 500000:
        # Step 6.1: Check if currentIndex in is_active is True
        if is_active[current_index]:
            # Step 6.1.a: Set the currentIndex element to False
            is_active[current_index] = False
        
        # Step 6.2: Increment the increment variable
        increment += 1
        
        # Step 6.3: Update currentIndex with the new increment value
        current_index = (current_index + increment) % n
    
    # Step 7: Create a list activeElements containing only True values
    active_elements = [value for value in is_active if value]
    
    # Step 8: If the length of activeElements is 0, output "YES"
    if len(active_elements) == 0:
        print("YES")
    else:
        # Step 9: Otherwise, output "NO"
        print("NO")

# Call the function to execute the program
check_active_values()
