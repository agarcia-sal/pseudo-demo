def main():
    # Step 2: Input
    total_numbers = int(input())

    # Step 3: Initialize the availability list
    is_number_available = [True] * total_numbers  # List to track available numbers

    # Step 4: Initialize step count and current index
    step_count = 1
    current_index = 0

    # Step 6: Loop iteration for elimination
    while step_count <= 500000:
        if is_number_available[current_index]:
            is_number_available[current_index] = False  # Eliminate the number
        
        step_count += 1
        current_index = (current_index + step_count) % total_numbers  # Update index

    # Step 7: Create a new list of available numbers
    available_numbers = [num for num in is_number_available if num]

    # Step 8: Check availability
    if len(available_numbers) == 0:
        print("YES")  # All numbers eliminated
    else:
        print("NO")  # Some numbers are still available

# Entry point of the program
if __name__ == "__main__":
    main()
