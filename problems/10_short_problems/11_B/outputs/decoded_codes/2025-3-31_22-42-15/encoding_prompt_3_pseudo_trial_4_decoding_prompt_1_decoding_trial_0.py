# Begin

# Input: Receive an integer input and take its absolute value
inputNumber = abs(int(input()))

# Initialize a variable to track iterative counting
index = 0

# Start an infinite loop to find the solution
while True:
    # Calculate the sum of the first 'index' natural numbers
    sumToIndex = (index * (index + 1)) // 2

    # Determine the difference from the target input
    difference = sumToIndex - inputNumber

    # Check if the current sum equals the target input
    if sumToIndex == inputNumber:
        # Output the current index which is the result
        print(index)
        break

    # Check if the current sum exceeds the target input
    elif sumToIndex > inputNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            # Output the current index which is the result
            print(index)
            break

    # Increment the index to check the next natural number
    index += 1

# End
