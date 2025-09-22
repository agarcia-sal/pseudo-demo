# Initialize Input
n = abs(int(input()))

# Set Initial Values
index = 0

# Repeat Until Found
while True:
    # Calculate Sum
    sumUpToIndex = (index * (index + 1)) / 2

    # Determine the Difference
    difference = sumUpToIndex - n

    # Check for Equality
    if sumUpToIndex == n:
        print(index)
        break

    # Check for Greater Than Condition
    if sumUpToIndex > n:
        if difference % 2 == 0:
            print(index)
            break

    # Increment Index
    index += 1
