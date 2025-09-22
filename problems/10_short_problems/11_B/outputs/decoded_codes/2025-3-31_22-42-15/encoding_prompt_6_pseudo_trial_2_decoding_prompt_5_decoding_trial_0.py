# Function to determine the index of the triangular number corresponding to the input
def find_triangular_number():
    # Input: Get an integer from the user and convert it to its absolute value
    number = abs(int(input()))
    
    # Initialize: Start a counter variable
    index = 0

    # Loop indefinitely: Continue checking for triangular number conditions
    while True:
        # Calculate Triangular Number using the formula n*(n+1)/2
        triangular_sum = (index * (index + 1)) // 2
        
        # Calculate Difference from the input number
        difference = triangular_sum - number
        
        # Check Conditions
        if triangular_sum == number:
            # Print index if a triangular number is found
            print(index)
            break
        elif triangular_sum > number and difference % 2 == 0:
            # Print index if the difference is even
            print(index)
            break
        
        # Increment Counter
        index += 1

# Call the function to execute
find_triangular_number()
