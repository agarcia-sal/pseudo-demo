def find_smallest_integer():
    # Step 1: Receive Input
    target_sum = int(input())

    # Step 2: Initialize Variables
    current_index = 0

    # Step 3: Infinite Loop
    while True:
        # Step 3.1: Calculate the Sum
        current_sum = (current_index * (current_index + 1)) // 2  # Use integer division

        # Step 3.2: Calculate the Difference
        surplus = current_sum - target_sum

        # Step 3.3: Check for Exact Match
        if current_sum == target_sum:
            print(current_index)
            break  # Exit the loop if we found the match

        # Step 3.4: Check for Surplus Condition
        if surplus > 0 and surplus % 2 == 0:
            print(current_index)
            break  # Exit the loop if surplus can be evenly divided

        # Step 3.5: Increment Index
        current_index += 1

# Call the function to execute
find_smallest_integer()
