# Step 1: Get absolute integer input value 'n' from the user
n = abs(int(input()))  # Using abs to ensure it's non-negative

# Step 2: Set initial values
index = 0  # Start checking from 0

# Step 3: Create an infinite loop to find the solution
while True:
    # Step 4: Calculate the sum of the first 'index' integers
    sum_up_to_index = (index * (index + 1)) / 2  # Using the formula for sum of first 'index' integers

    # Step 5: Calculate the difference
    difference = sum_up_to_index - n

    # Step 6: Check for equality
    if sum_up_to_index == n:
        print(index)  # Print the current index if it equals n
        break  # Exit the loop

    # Step 7: Check if sum_up_to_index is greater than n
    if sum_up_to_index > n:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print the current index if the difference is even
            break  # Exit the loop

    # Step 8: Increment index for the next check
    index += 1  # Move to the next integer
