# Begin program
# Step 1: Read integer input from the user and get its absolute value
absolute_value = abs(int(input()))

# Step 2: Initialize current index to 0
current_index = 0

# Step 3: Start an indefinite loop
while True:
    # Step 4: Calculate the sum of the first current_index natural numbers
    sum_of_numbers = (current_index * (current_index + 1)) // 2  # Using integer division
    
    # Step 5: Calculate the difference
    difference = sum_of_numbers - absolute_value
    
    # Step 6: Check if sum_of_numbers equals absolute_value
    if sum_of_numbers == absolute_value:
        print(current_index)  # Output current_index
        break  # Exit loop
        
    # Step 7: Check if sum_of_numbers is greater than absolute_value
    elif sum_of_numbers > absolute_value:
        # Step 8: If the difference is even
        if difference % 2 == 0:
            print(current_index)  # Output current_index
            break  # Exit loop
    
    # Step 9: Increment current_index by 1
    current_index += 1

# End of program
