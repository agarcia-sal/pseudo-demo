# Receive an integer input and store its absolute value
absoluteValue = abs(int(input()))

# Initialize index to track the current integer being evaluated
index = 0

# Enter an infinite loop to evaluate conditions based on index
while True:
    # Calculate the sum of the first index integers
    sumOfIntegers = index * (index + 1) // 2

    # Calculate the difference between sumOfIntegers and absoluteValue
    difference = sumOfIntegers - absoluteValue

    # Check if sumOfIntegers is equal to absoluteValue
    if sumOfIntegers == absoluteValue:
        print(index)  # Print index when both are equal
        break  # Exit the loop

    # Check if sumOfIntegers is greater than absoluteValue
    if sumOfIntegers > absoluteValue:
        # Check if difference is an even number
        if difference % 2 == 0:
            print(index)  # Print index when conditions are met
            break  # Exit the loop

    # Increase index by 1 to evaluate the next integer
    index += 1
