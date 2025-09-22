# Get the absolute value of user input
number = abs(int(input()))

# Initialize the counter variable
index = 0

# Loop indefinitely to find the triangular number condition
while True:
    # Calculate the Triangular Number
    triangularSum = (index * (index + 1)) // 2

    # Calculate the Difference
    difference = triangularSum - number

    # Check Conditions
    if triangularSum == number:
        print(index)  # number is a triangular number
        break
    elif triangularSum > number:
        if difference % 2 == 0:
            print(index)  # number can be represented as a triangular number with adjustment
            break

    # Increment Counter
    index += 1
