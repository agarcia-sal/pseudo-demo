# Get the absolute value of the user input and convert it to an integer
absolute_value = abs(int(input()))

# Initialize a counter variable
index = 0

# Loop indefinitely until a break condition is met
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_natural_numbers = (index * (index + 1)) // 2
    
    # Calculate the difference between the sum and the input value
    difference = sum_natural_numbers - absolute_value
    
    # Check if the sum equals the input value
    if sum_natural_numbers == absolute_value:
        # If they are equal, print the current index
        print(index)
        break
    
    # Check if the sum is greater than the input value
    elif sum_natural_numbers > absolute_value:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # If it is even, print the current index
            print(index)
            break
    
    # Increment the index for the next iteration
    index += 1
