# Get the absolute value of user input as an integer
number = abs(int(input()))

# Initialize a variable to keep track of index
index = 0

# Start an infinite loop to process the logic
while True:
    # Calculate the sum of the first 'index' natural numbers using the formula
    sum_of_natural_numbers = (index * (index + 1)) // 2
    
    # Calculate the difference between the sum and the input number
    difference = sum_of_natural_numbers - number
    
    # Check if the calculated sum matches the input number
    if sum_of_natural_numbers == number:
        # If they match, print the current index and exit
        print(index)
        break
    
    # Check if the sum has exceeded the input number
    elif sum_of_natural_numbers > number:
        # Check if the difference is even
        if difference % 2 == 0:
            # If the difference is even, print the current index and exit
            print(index)
            break
    
    # Increment the index for the next iteration
    index += 1
