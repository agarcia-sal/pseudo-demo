# Read a positive integer input from the user
target_triangle_number = int(input())

# Initialize the index to zero
index = 0

# Infinite loop to evaluate potential triangle numbers
while True:
    # Calculate the triangle number for the current index
    triangle_number = (index * (index + 1)) / 2
    
    # Calculate the difference between the triangle number and the target
    difference = triangle_number - target_triangle_number
    
    # Check if the triangle number matches the target
    if triangle_number == target_triangle_number:
        print(index)  # Output the current index
        break  # Terminate the loop
        
    # If the triangle number is greater than the target
    if triangle_number > target_triangle_number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)  # Output the current index
            break  # Terminate the loop
            
    # Increment index to check the next triangle number
    index += 1
