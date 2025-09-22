def find_smallest_integer():
    # Step 1: Receive Input
    target_value = abs(int(input()))

    # Step 2: Initialize Variables
    index = 0

    # Step 3: Infinite Loop
    while True:
        # Step 3.1: Calculate Sum
        current_sum = (index * (index + 1)) // 2  # Using integer division

        # Step 3.2: Calculate Difference
        diff = current_sum - target_value

        # Step 3.3: Check for Equality
        if current_sum == target_value:
            print(index)
            break

        # Step 3.4: Check for Greater Sum
        if current_sum > target_value:
            if diff % 2 == 0:  # Checking if diff is even
                print(index)
                break

        # Step 3.5: Increment Index
        index += 1

# Run the function
find_smallest_integer()
