# Function to find the index of the triangle number
def find_triangle_number_index():
    # Read user input and convert it to a positive integer
    target_triangle_number = int(input())
    
    # Initialize the index for triangle numbers
    index = 0
    
    # Infinite loop to evaluate potential triangle numbers
    while True:
        # Calculate the triangle number for the current index
        triangle_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangle number and target
        difference = triangle_number - target_triangle_number
        
        # Check if the calculated triangle number is equal to the target
        if triangle_number == target_triangle_number:
            print(index)
            break
        
        # Check if the triangle number is greater than the target
        if triangle_number > target_triangle_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next triangle number
        index += 1

# Example test case (user is expected to provide input):
# This call should be included in a main block or at the end of the script to execute
# Uncomment the following line to run the function
# find_triangle_number_index()
