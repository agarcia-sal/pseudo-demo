# Input: Take a positive integer from the user
targetTriangleNumber = int(input())

# Initialize the index variable
index = 0

# Infinite loop to evaluate triangle numbers
while True:
    # Calculate the triangle number for the current index
    triangleNumber = (index * (index + 1)) / 2
    
    # Calculate the difference from the target triangle number
    difference = triangleNumber - targetTriangleNumber
    
    # Check if the calculated triangle number matches the target
    if triangleNumber == targetTriangleNumber:
        print(index)  # Output the current index
        break  # Terminate the loop
    
    # Check if the triangle number is greater than the target
    if triangleNumber > targetTriangleNumber:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)  # Output the current index
            break  # Terminate the loop
    
    # Increment index for the next iteration
    index += 1
