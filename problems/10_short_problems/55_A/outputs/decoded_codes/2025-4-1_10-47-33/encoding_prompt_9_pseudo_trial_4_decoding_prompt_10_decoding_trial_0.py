def can_all_elements_be_marked(n):
    # Step 2: Initialize the marked list with all elements set to True
    marked = [True] * n
    
    # Step 3: Initialize counters
    current_index = 0
    step_size = 1

    # Step 4: Iterative marking
    while step_size <= 500000:
        # Check if the current index is marked
        if marked[current_index]:
            # Mark the current index as False
            marked[current_index] = False

        # Increment the step size
        step_size += 1
        
        # Calculate the next index to check, using modulo to wrap around
        current_index = (current_index + step_size) % n

    # Step 5: Check remaining True values
    remaining_true = [value for value in marked if value]

    # Step 6: Output the result
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Reading input
n = int(input())
can_all_elements_be_marked(n)


# Edge case tests
n = 1  # Should return "NO"
n = 2  # Should return "NO"
n = 3  # Should return "NO"
n = 500000  # Should return "NO"

# Call the function for different values of n to observe results
print("Test Case 1:")
can_all_elements_be_marked(1)  # Expected: NO

print("Test Case 2:")
can_all_elements_be_marked(2)  # Expected: NO

print("Test Case 3:")
can_all_elements_be_marked(3)  # Expected: NO

print("Test Case 4:")
can_all_elements_be_marked(500000)  # Expected: NO
