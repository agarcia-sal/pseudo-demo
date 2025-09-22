# Start the program

# Step 2: Get input from the user and store the absolute value in target_sum
target_sum = abs(int(input()))

# Step 3: Initialize the index to 0
index = 0

# Step 4: Repeat indefinitely
while True:
    # Step 4a: Calculate the sum of the first 'index' natural numbers
    current_sum = (index * (index + 1)) / 2
    
    # Step 4b: Calculate the difference between current_sum and target_sum
    difference = current_sum - target_sum
    
    # Step 4c: Check if current_sum equals target_sum
    if current_sum == target_sum:
        print(index)  # Step 4c: Print current value of index
        break  # Exit the loop
    
    # Step 4d: Check if current_sum is greater than target_sum
    if current_sum > target_sum:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)  # Step 4d: Print current value of index
            break  # Exit the loop
            
    # Step 4e: Increment index by 1
    index += 1

# End of the program
