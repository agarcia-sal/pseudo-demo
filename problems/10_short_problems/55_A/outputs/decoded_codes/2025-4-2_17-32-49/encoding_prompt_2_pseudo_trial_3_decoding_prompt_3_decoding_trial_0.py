def number_availability():
    # Step 2: Read an integer value called totalNumbers
    total_numbers = int(input())
    
    # Step 3: Initialize the availability list
    is_number_available = [True] * total_numbers
    
    # Step 4: Initialize stepCount and currentIndex
    step_count = 1
    current_index = 0
    
    # Step 6: Repeat until stepCount exceeds 500,000
    while step_count <= 500000:
        # Check if the current number is available
        if is_number_available[current_index]:
            # Mark the number as not available
            is_number_available[current_index] = False
            
        # Increment stepCount
        step_count += 1
        
        # Update currentIndex for the next step using modulo
        current_index = (current_index + step_count) % total_numbers
    
    # Step 7: Generate the list of available numbers
    available_numbers = [i for i in range(total_numbers) if is_number_available[i]]
    
    # Step 8: Check availability and output result
    if len(available_numbers) == 0:
        print("YES")  # All numbers have been eliminated
    else:
        print("NO")   # There are still available numbers

# Call the function to execute the logic
number_availability()
