# Receive Input
inputNumber = abs(int(input()))  # Convert input to absolute value

# Initialize Variables
index = 0

# Continuous Loop
while True:
    # Calculate the triangular number
    triangularNumber = (index * (index + 1)) // 2  # Use integer division

    # Compute the difference
    difference = triangularNumber - inputNumber

    # Check Conditions
    if triangularNumber == inputNumber:
        print(index)
        break
    elif triangularNumber > inputNumber:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)
            break

    # Increment index by 1
    index += 1
