# Get a number from the user and convert it to an integer
targetNumber = abs(int(input()))

# Initialize a counter variable
index = 0

# Enter an infinite loop
while True:
    # Calculate the sum of the first index natural numbers
    sumOfFirstIndex = (index * (index + 1)) // 2
    
    # Calculate the difference from the target number
    difference = sumOfFirstIndex - targetNumber

    # Check if the current sum equals the target number
    if sumOfFirstIndex == targetNumber:
        print(index)
        break

    # Check if the current sum exceeds the target number
    if sumOfFirstIndex > targetNumber:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)
            break

    # Increment the counter variable
    index += 1
