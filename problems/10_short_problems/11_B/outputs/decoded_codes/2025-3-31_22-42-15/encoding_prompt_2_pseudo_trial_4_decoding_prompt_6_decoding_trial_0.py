# Start

# Step 2: Read an integer value from the user and take its absolute value.
target_number = abs(int(input()))

# Step 3: Initialize index to 0
index = 0

# Step 4: Loop indefinitely
while True:
    # Calculate currentSum using the formula for the sum of the first 'index' natural numbers
    current_sum = (index * (index + 1)) // 2
    
    # Calculate the difference
    difference = current_sum - target_number
    
    # Step 5: Check conditions
    if current_sum == target_number:
        # If currentSum is equal to targetNumber, print index and exit the loop
        print(index)
        break
    elif current_sum > target_number:
        # If currentSum is greater than targetNumber, check if difference is even
        if difference % 2 == 0:
            print(index)
            break
    
    # Step 6: Increment index by 1
    index += 1

# End
