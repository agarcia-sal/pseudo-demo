# Get user input and convert to absolute integer
integer_value = abs(int(input()))

# Initialize a counter variable
index = 0

# Create an infinite loop to find a solution
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_of_natural_numbers = (index * (index + 1)) // 2
    
    # Calculate the difference between the calculated sum and the input value
    difference = sum_of_natural_numbers - integer_value
    
    # Check if the calculated sum matches the input value
    if sum_of_natural_numbers == integer_value:
        print(index)  # Print the current index
        break  # Exit the loop
    
    # Check if the calculated sum exceeds the input value
    elif sum_of_natural_numbers > integer_value:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print the current index
            break  # Exit the loop
    
    # Increment the index for the next iteration
    index += 1
