# Importing the necessary function
def absolute_value(num):
    return abs(num)

# BEGIN
# Read an integer input, taking its absolute value
absoluteValue = absolute_value(int(input()))

# Initialize a counter variable
counter = 0

# Loop indefinitely until a break condition is met
while True:
    # Calculate the sum of the first 'counter' integers
    currentSum = (counter * (counter + 1)) // 2

    # Calculate the difference between currentSum and absoluteValue
    difference = currentSum - absoluteValue

    # Check if the currentSum equals the absoluteValue
    if currentSum == absoluteValue:
        print(counter)  # Output the counter value
        break  # Exit the loop

    # Check if currentSum exceeds absoluteValue
    elif currentSum > absoluteValue:
        # Check if the difference is even
        if difference % 2 == 0:
            print(counter)  # Output the counter value
            break  # Exit the loop

    # Increment the counter for the next iteration
    counter += 1

# END
