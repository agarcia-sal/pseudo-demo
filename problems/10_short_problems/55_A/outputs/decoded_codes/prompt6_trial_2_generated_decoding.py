# Step 1: Read an integer value n from the user input
n = int(input())  

# Step 2: Create a boolean list 'is_active' of size n and initialize all values to True
is_active = [True] * n  

# Step 3: Set variable 'current_index' to 0
current_index = 0  

# Step 4: Set variable 'step' to 1
step = 1  

# Step 5: While 'step' is less than or equal to 500000
while step <= 500000:
    # Step 5a: Check if current index is active
    if is_active[current_index]:
        # Step 5a.i: Mark the current_index as inactive
        is_active[current_index] = False  
    
    # Step 5b: Increment 'step' by 1
    step += 1
    
    # Step 5c: Move to the next index cyclically
    current_index = (current_index + step) % n  

# Step 6: Create a list 'remaining_active' with all elements from 'is_active' that are still True
remaining_active = [active for active in is_active if active]  

# Step 7: Check if there are any remaining active positions
if len(remaining_active) == 0:
    # Step 7a: Print "YES" if all positions are inactive
    print("YES")  
else:
    # Step 7b: Print "NO" if some positions are still active
    print("NO")  
