# This program finds the index of a triangle number that matches a target input
# or satisfies a condition based on the difference being even.

# Get user input and convert to positive integer
targetTriangleNumber = int(input())
if targetTriangleNumber <= 0:
    raise ValueError("Input must be a positive integer.")

index = 0  # Initialize index to zero

while True:  # Start an infinite loop to evaluate triangle numbers
    # Calculate the current triangle number
    triangleNumber = (index * (index + 1)) // 2  # Use integer division

    # Calculate the difference from the target triangle number
    difference = triangleNumber - targetTriangleNumber

    # Check if the calculated triangle number matches the target
    if triangleNumber == targetTriangleNumber:
        print(index)  # Output the index
        break  # Exit the loop

    # Check if the triangle number is greater than the target
    if triangleNumber > targetTriangleNumber:
        # If the difference is even
        if difference % 2 == 0:
            print(index)  # Output the index
            break  # Exit the loop

    index += 1  # Increment the index to evaluate the next triangle number
