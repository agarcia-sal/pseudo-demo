# Step 1: Get user input
input_number = abs(int(input()))  # Convert user input to absolute integer

# Step 2: Initialize loop variable
index = 0

# Step 3: Begin an infinite loop to find the solution
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_natural_numbers = (index * (index + 1)) / 2
    
    # Calculate the difference between the sum and input_number
    difference = sum_natural_numbers - input_number

    # Step 4: Check if the current sum equals the input number
    if sum_natural_numbers == input_number:
        print(index)  # Print the index if sum equals input number
        break  # Exit the loop
    
    # Step 5: Check if the current sum exceeds the input number
    elif sum_natural_numbers > input_number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print the index if the difference is even
            break  # Exit the loop
    
    # Increment the loop variable
    index += 1  # Move to the next index
