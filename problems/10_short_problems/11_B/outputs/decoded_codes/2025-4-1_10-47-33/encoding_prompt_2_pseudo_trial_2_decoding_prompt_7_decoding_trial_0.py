# Function to find the index of a triangle number
def find_triangle_number_index():
    # Step 1: Get positive integer input from the user
    targetTriangleNumber = int(input())
    
    # Step 2: Initialize index to zero
    index = 0
    
    # Infinite loop to evaluate potential triangle numbers
    while True:
        # Step 3a: Calculate the triangle number for the current index
        triangleNumber = (index * (index + 1)) // 2  # Using integer division
        
        # Step 3b: Compute the difference between triangleNumber and target
        difference = triangleNumber - targetTriangleNumber
        
        # Step 3c: Check if triangleNumber equals targetTriangleNumber
        if triangleNumber == targetTriangleNumber:
            print(index)  # Output the current index
            break  # Terminate the loop
        
        # Step 3d: Check if triangleNumber is greater than targetTriangleNumber
        if triangleNumber > targetTriangleNumber:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Terminate the loop
        
        # Step 3e: Increment index for next evaluation
        index += 1

# Execute the function
find_triangle_number_index()
