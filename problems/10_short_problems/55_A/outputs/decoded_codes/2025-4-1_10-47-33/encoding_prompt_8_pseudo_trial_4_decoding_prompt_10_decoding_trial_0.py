def main():
    # Step 1: Read Input for the total number of entries
    total_numbers = int(input())

    # Step 2: Initialize the statusList with all entries set to True
    status_list = [True] * total_numbers

    # Step 3: Set Initial Indices
    current_index = 0
    step = 1

    # Step 4: Loop Until Step Reaches Limit
    while step <= 500000:
        # a. Mark the current index as False if it is True
        if status_list[current_index]:
            status_list[current_index] = False
        
        # b. Increment the step
        step += 1
        
        # c. Update the current index circularly
        current_index = (current_index + step) % total_numbers

    # Step 5: Check Remaining True Values
    remaining_true_values = [value for value in status_list if value]

    # Step 6: Output Result Based on Remaining True Values
    if len(remaining_true_values) == 0:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
