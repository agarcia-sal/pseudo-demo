# Get the Absolute Value of Input
targetNumber = abs(int(input()))

# Initialize a Count Variable
count = 0

# Start an Infinite Loop to Find Solution
while True:
    # Calculate the Sum of the First `count` Numbers
    sumOfIntegers = (count * (count + 1)) // 2

    # Calculate the Difference from the Target Number
    difference = sumOfIntegers - targetNumber

    # Check Conditions for Output
    if sumOfIntegers == targetNumber:
        print(count)
        break
    elif sumOfIntegers > targetNumber and difference % 2 == 0:
        print(count)
        break

    # Increment the Count
    count += 1
