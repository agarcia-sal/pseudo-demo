def main():
    # Step 1: Input an integer value called totalNumbers
    total_numbers = int(input())

    # Step 2: Create a list called isNumberAvailable initialized to True
    is_number_available = [True] * total_numbers

    # Step 3: Initialize stepCount and currentIndex
    step_count = 1
    current_index = 0

    # Step 4: Loop while stepCount is less than or equal to 500,000
    while step_count <= 500000:
        # Check if the current number is available
        if is_number_available[current_index]:
            # Mark the number as unavailable
            is_number_available[current_index] = False
        
        # Increment stepCount
        step_count += 1
        
        # Update the currentIndex
        current_index = (current_index + step_count) % total_numbers
    
    # Step 5: Create availableNumbers list
    available_numbers = [num for num in is_number_available if num]

    # Step 6: Check availability
    if len(available_numbers) == 0:
        print("YES")  # All numbers eliminated
    else:
        print("NO")   # Some numbers are still available

if __name__ == "__main__":
    main()
