# Step 1: Get input from the user, expecting a non-negative integer
target_sum = int(input())

# Step 2: Initialize current index variable to 0
current_index = 0

# Step 3: Begin an infinite loop to find a solution
while True:
    # Step 4: Calculate the sum of the first current_index integers
    current_sum = (current_index * (current_index + 1)) // 2  # Using integer division

    # Step 5: Calculate the surplus
    surplus = current_sum - target_sum

    # Step 6: Check if the current sum equals the target sum
    if current_sum == target_sum:
        print(current_index)  # Print the current index as the solution
        break  # Exit the loop

    # Step 7: Check if the current sum exceeds the target sum
    if current_sum > target_sum:
        # Step 8: Check if the surplus can be evenly divided by 2
        if surplus % 2 == 0:
            print(current_index)  # Print the current index as the solution
            break  # Exit the loop

    # Step 9: Increment the current index to process the next integer
    current_index += 1
