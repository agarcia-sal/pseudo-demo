# Start of the program

# Read an integer input from the user and take its absolute value.
userInput = abs(int(input()))

# Initialize a variable to keep track of the current index.
index = 0

# Continuously loop until a condition is met.
while True:
    # Calculate the sum of the first 'index' integers using the formula for the sum of an arithmetic series.
    sum = (index * (index + 1)) // 2  # Use // for integer division
    
    # Determine the difference between the calculated sum and the user input.
    difference = sum - userInput
    
    # Check if the calculated sum is equal to the user input.
    if sum == userInput:
        # Print the current index and exit the loop if the sums are equal.
        print(index)
        break
    
    # Check if the calculated sum exceeds the user input.
    elif sum > userInput:
        # If the difference is even, print the current index and exit the loop.
        if difference % 2 == 0:
            print(index)
            break
    
    # Increment the index to check the next integer in the next iteration.
    index += 1
