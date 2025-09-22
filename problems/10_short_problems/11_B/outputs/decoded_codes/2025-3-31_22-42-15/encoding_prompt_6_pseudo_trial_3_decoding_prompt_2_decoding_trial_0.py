# Read an integer input from the user and take its absolute value.
userInput = abs(int(input()))

# Initialize a variable to keep track of the current index.
index = 0

# Continuously loop until a condition is met.
while True:
    # Calculate the sum of the first 'index' integers using the formula for the sum of an arithmetic series.
    sum_value = (index * (index + 1)) // 2
    
    # Determine the difference between the calculated sum and the user input.
    difference = sum_value - userInput
    
    # Check if the calculated sum is equal to the user input.
    if sum_value == userInput:
        # If they are equal, print the current index and exit the loop.
        print(index)
        break
    
    # Check if the calculated sum exceeds the user input.
    elif sum_value > userInput:
        # If the difference is even, print the current index and exit the loop.
        if difference % 2 == 0:
            print(index)
            break
    
    # Increment the index to check the next integer in the next iteration.
    index += 1
