# Get Input: prompt user for input and convert it to an absolute integer
targetValue = abs(int(input()))

# Initialize Variables
index = 0

# Loop Indefinitely
while True:
    # Calculate the sum of the first 'index' integers
    currentSum = (index * (index + 1)) // 2  # Use integer division to avoid float results

    # Calculate the difference between currentSum and targetValue
    difference = currentSum - targetValue

    # Check Conditions
    if currentSum == targetValue:
        print(index)
        break  # Exit the loop if the condition is met
    elif currentSum > targetValue:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)
            break  # Exit the loop if the condition is met

    # Increment index by 1 for the next iteration
    index += 1
