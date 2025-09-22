# Step 1: Read an integer input from the user, taking the absolute value
user_input = abs(int(input()))
index = 0  # Initialize index

# Step 2: Infinite loop to find the required index
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_of_natural_numbers = (index * (index + 1)) // 2  # Using integer division
    
    # Calculate the difference from the user input
    difference = sum_of_natural_numbers - user_input
    
    # Step 3: Check if we found the desired sum
    if sum_of_natural_numbers == user_input:
        print(index)  # Output the index
        break  # Exit the loop
    
    # Step 4: If sum is greater than user input
    elif sum_of_natural_numbers > user_input:
        # Step 5: Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the index
            break  # Exit the loop
    
    # Step 6: Increment index for the next iteration
    index += 1
