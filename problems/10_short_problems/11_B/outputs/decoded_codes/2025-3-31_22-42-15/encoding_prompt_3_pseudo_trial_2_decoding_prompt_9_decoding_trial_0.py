# Start of the program

# Step 1: Get user input
input_number = abs(int(input()))  # Convert user input to an integer and take the absolute value

# Step 2: Initialize loop variable
index = 0

# Step 3: Begin an infinite loop to find the solution
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_of_natural_numbers = (index * (index + 1)) // 2  # Use integer division for accuracy

    # Calculate the difference between the sum and input_number
    difference = sum_of_natural_numbers - input_number

    # Step 4: Check if the current sum equals the input_number
    if sum_of_natural_numbers == input_number:
        print(index)  # Print the index
        break  # Exit the loop

    # Step 5: Check if the current sum exceeds the input_number
    elif sum_of_natural_numbers > input_number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print the index
            break  # Exit the loop

    # Increment the loop variable
    index += 1  # Move to the next index
