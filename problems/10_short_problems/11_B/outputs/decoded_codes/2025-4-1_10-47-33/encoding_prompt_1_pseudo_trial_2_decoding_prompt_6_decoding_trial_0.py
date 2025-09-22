# Step 1: Import the required function for absolute value
# In this case, it is not necessary as Python provides built-in abs()

# Step 2: Input Handling
absolute_input = abs(int(input()))  # Read a number and store its absolute value

# Step 3: Initialize a Counter
index = 0  # This will keep track of the current integer

# Step 4: Infinite Loop for Calculation
while True:
    # Calculate the sum of the first 'index' integers
    current_sum = (index * (index + 1)) // 2  # Using integer division

    # Calculate the difference between current_sum and absolute_input
    difference = current_sum - absolute_input

    # Check Conditions
    if current_sum == absolute_input:
        print(index)  # Output the value of index
        break  # Exit the loop
    elif current_sum > absolute_input:
        if difference % 2 == 0:  # Check if difference is an even number
            print(index)  # Output the value of index
            break  # Exit the loop

    # Increment the Counter
    index += 1  # Increase index by 1 to check the next integer
