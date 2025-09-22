# Begin the program

# Step 2: Get the absolute integer value from user input
input_value = abs(int(input()))  # Store absolute value of the user input

# Step 3: Initialize a counter
current_index = 0  # Starting index for natural numbers

# Step 4: Repeat indefinitely (loop until a condition is met)
while True:
    # Step 4a: Calculate the sum of the first current_index natural numbers
    sum_of_naturals = (current_index * (current_index + 1)) // 2  # Using // for integer division
    
    # Step 4b: Calculate the difference from input_value
    difference = sum_of_naturals - input_value
    
    # Step 4c: Check if sum_of_naturals equals input_value
    if sum_of_naturals == input_value:
        print(current_index)  # Output current_index
        break  # Exit the loop
    
    # Step 4d: Check if sum_of_naturals is greater than input_value
    if sum_of_naturals > input_value:
        # Check if the difference is an even number
        if difference % 2 == 0:  # If difference is even
            print(current_index)  # Output current_index
            break  # Exit the loop
    
    # Step 4e: Increment current_index by 1
    current_index += 1  # Move to the next natural number

# End of the program
