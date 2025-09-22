# Step 1: Read an integer value from the user
target_number = abs(int(input()))  # Calculate the absolute value of the input

# Step 2: Initialize the counter variable
index = 0

# Step 3: Start an infinite loop
while True:
    # Calculate the sum of the first index natural numbers
    current_sum = index * (index + 1) // 2
    
    # Calculate the difference between current_sum and target_number
    difference = current_sum - target_number
    
    # Step 4: Check Conditions
    if current_sum == target_number:
        print(index)  # Print the value of index
        break  # Exit the loop
    elif current_sum > target_number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print the value of index
            break  # Exit the loop
    
    # Increment the value of index by 1
    index += 1
