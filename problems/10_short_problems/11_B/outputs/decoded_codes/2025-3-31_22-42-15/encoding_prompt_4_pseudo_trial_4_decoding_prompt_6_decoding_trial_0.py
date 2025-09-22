# Begin the program to find the index where the sum of integers equals or surpasses the absolute input number

# Prompt user for input and store the absolute value of the integer
number = abs(int(input()))  # Read input and convert to absolute integer

# Initialize a counter variable
index = 0

# Infinite loop to find the solution
while True:
    # Calculate the sum of the first 'index' integers using the formula for the sum of the first n natural numbers
    total_sum = (index * (index + 1)) / 2
    
    # Calculate the difference between the sum and the input number
    difference = total_sum - number
    
    # Check if the sum equals the input number
    if total_sum == number:
        print(index)  # Output the index
        break  # Exit the loop
    
    # Check if the sum exceeds the input number
    elif total_sum > number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the index
            break  # Exit the loop
    
    # Increment the counter variable
    index += 1
