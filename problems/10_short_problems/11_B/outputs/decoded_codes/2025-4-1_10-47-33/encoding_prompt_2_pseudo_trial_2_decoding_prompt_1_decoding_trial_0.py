# Input
targetTriangleNumber = int(input())  # Read input and convert to integer

# Initialize index
index = 0  # Starting index for triangle numbers

# Infinite loop to calculate triangle numbers
while True:
    # Calculate the triangle number
    triangleNumber = (index * (index + 1)) / 2  
    
    # Calculate the difference
    difference = triangleNumber - targetTriangleNumber  
    
    # Check if triangle number is equal to the target triangle number
    if triangleNumber == targetTriangleNumber:
        print(index)  # Output the index
        break  # Terminate the loop

    # Check if triangle number is greater than the target
    elif triangleNumber > targetTriangleNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the index
            break  # Terminate the loop
    
    # Increment index for next iteration
    index += 1
