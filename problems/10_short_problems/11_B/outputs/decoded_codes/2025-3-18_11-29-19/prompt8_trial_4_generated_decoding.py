# Begin the Program

# Receive Input
number = int(input())
absoluteNumber = abs(number)

# Initialize the Counter
index = 0

# Loop Until a Condition is Met
while True:
    # Calculate the triangular number
    triangularNumber = (index * (index + 1)) // 2
    # Calculate the difference from the input
    difference = triangularNumber - absoluteNumber

    # Check Conditions
    if triangularNumber == absoluteNumber:
        print(index)
        break
    elif triangularNumber > absoluteNumber:
        if difference % 2 == 0:
            print(index)
            break

    # Increment index
    index += 1

# End the Program
