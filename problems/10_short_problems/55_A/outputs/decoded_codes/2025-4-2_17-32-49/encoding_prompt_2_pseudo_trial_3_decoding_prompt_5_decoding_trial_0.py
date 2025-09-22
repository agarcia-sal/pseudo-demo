# This function checks the availability of numbers after a specific elimination process

def check_number_availability():
    # Step 2: Read an integer value for totalNumbers
    total_numbers = int(input())
    
    # Step 3: Create a list to track the availability of each number
    is_number_available = [True] * total_numbers
    
    # Step 4: Initialize stepCount to track the current step in the elimination process
    step_count = 1
    
    # Step 5: Initialize currentIndex to indicate the current position
    current_index = 0
    
    # Step 6: Loop until stepCount exceeds 500,000
    while step_count <= 500000:
        # Check if the current index in is_number_available is True
        if is_number_available[current_index]:
            # Set that position to False, indicating the number is eliminated
            is_number_available[current_index] = False
        
        # Increment stepCount
        step_count += 1
        
        # Update currentIndex using the specified formula
        current_index = (current_index + step_count) % total_numbers
    
    # Step 7: Create a list of available numbers that are still True
    available_numbers = [num for num in is_number_available if num]
    
    # Step 8: Check the availability and output the result
    if len(available_numbers) == 0:
        print("YES")  # All numbers have been eliminated
    else:
        print("NO")   # There are still available numbers

# Call the function to check number availability
check_number_availability()
