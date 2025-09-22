# Find Triangle Number Index

# Input: Get the target triangle number
targetTriangleNumber = int(input())

# Initialize index
index = 0

# Infinite loop to find the triangle number index
while True:
    # Calculate the triangle number for the current index
    triangleNumber = (index * (index + 1)) // 2
    
    # Calculate the difference between triangle number and target
    difference = triangleNumber - targetTriangleNumber
    
    # Check if the triangle number matches the target
    if triangleNumber == targetTriangleNumber:
        print(index)
        break
        
    # Check if the triangle number exceeds the target
    if triangleNumber > targetTriangleNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)
            break
            
    # Increment index for the next iteration
    index += 1
