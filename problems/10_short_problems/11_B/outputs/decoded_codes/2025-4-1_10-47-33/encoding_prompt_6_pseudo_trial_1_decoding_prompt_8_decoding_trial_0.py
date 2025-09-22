# Read the absolute value of user input and convert it to an integer
userInput = abs(int(input()))
integerValue = userInput

# Initialize an index for iteration
index = 0

# Begin an infinite loop to process until we find the solution
while True:
    
    # Calculate the sum of the first 'index' integers
    sumOfIntegers = (index * (index + 1)) // 2
    
    # Calculate the difference between the current sum and the input value
    difference = sumOfIntegers - integerValue

    # Check if the current sum is exactly equal to the input value
    if sumOfIntegers == integerValue:
        # If equal, print the current index and exit the loop
        print(index)
        break

    # Check if the current sum is greater than the input value
    elif sumOfIntegers > integerValue:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # If the difference is even, print the current index and exit the loop
            print(index)
            break

    # Increment the index for the next iteration
    index += 1
