# Start by getting a number from the user
targetNumber = abs(int(input()))

# Initialize a counter variable
index = 0

# Enter an infinite loop
while True:
    # Calculate the sum of the first 'index' natural numbers
    sumOfFirstIndex = (index * (index + 1)) // 2  # Using integer division
    
    # Calculate the difference
    difference = sumOfFirstIndex - targetNumber

    # Check if the current sum equals the target number
    if sumOfFirstIndex == targetNumber:
        print(index)
        break

    # Check if the current sum exceeds the target number
    if sumOfFirstIndex > targetNumber:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)
            break

    # Increment the counter variable
    index += 1
