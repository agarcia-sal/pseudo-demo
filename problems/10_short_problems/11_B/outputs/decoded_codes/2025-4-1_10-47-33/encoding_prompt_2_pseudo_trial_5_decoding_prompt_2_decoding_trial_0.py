# Step 1: Receive input and store its absolute value
absoluteValue = abs(int(input()))

# Step 2: Initialize index
index = 0

# Step 3: Infinite loop to evaluate conditions based on index
while True:
    # Calculate the sum of the first index integers
    sumOfIntegers = index * (index + 1) // 2

    # Calculate the difference
    difference = sumOfIntegers - absoluteValue

    # Step 4: Check if sumOfIntegers equals absoluteValue
    if sumOfIntegers == absoluteValue:
        print(index)
        break

    # Step 5: Check if sumOfIntegers is greater than absoluteValue
    if sumOfIntegers > absoluteValue:
        # Check if difference is an even number
        if difference % 2 == 0:
            print(index)
            break

    # Increase index by 1 to evaluate the next integer
    index += 1
