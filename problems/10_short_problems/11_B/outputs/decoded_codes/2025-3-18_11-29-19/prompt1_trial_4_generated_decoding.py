# Get the absolute value of user input and convert it to an integer
number = abs(int(input()))

# Initialize a counter variable
index = 0

# Infinite loop to find the solution
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_of_natural_numbers = (index * (index + 1)) / 2
    
    # Calculate the difference between the sum and the input number
    difference = sum_of_natural_numbers - number
    
    # Check if the sum equals the input number
    if sum_of_natural_numbers == number:
        print(index)  # Found the direct match
        break  # Exit the loop
    
    # Check if the sum exceeds the input number
    elif sum_of_natural_numbers > number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)  # Found a solution
            break  # Exit the loop
    
    # Increment the index for the next iteration
    index += 1
