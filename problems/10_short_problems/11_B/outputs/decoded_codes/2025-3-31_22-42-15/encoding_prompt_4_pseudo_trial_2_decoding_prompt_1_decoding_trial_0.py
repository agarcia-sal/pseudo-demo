# BEGIN

# Get the absolute value of an integer from user input
number = abs(int(input()))

index = 0

# Infinite loop until a condition is met
while True:
    
    # Calculate the sum of the first 'index' natural numbers
    sum = (index * (index + 1)) // 2  # Use // for integer division
    
    # Calculate the difference between sum and number
    difference = sum - number
    
    # Check if the sum equals the number
    if sum == number:
        print(index)
        break
    
    # Check if the sum is greater than the number
    elif sum > number:
        
        # Check if the difference is even
        if difference % 2 == 0:  # Check if the difference is even
            print(index)
            break
    
    # Increment index for the next iteration
    index += 1

# END
