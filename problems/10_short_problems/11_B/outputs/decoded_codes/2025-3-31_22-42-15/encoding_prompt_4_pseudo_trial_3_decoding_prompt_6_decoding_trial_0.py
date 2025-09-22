# Function to find the triangular number
def find_triangle_number():
    # Read a number from user input
    n = int(input())
    
    # Take the absolute value of n
    n = abs(n)
    
    # Initialize the index variable 
    i = 0
    
    # Infinite loop to find the triangular number
    while True:
        # Calculate the triangular number using the formula
        s = (i * (i + 1)) // 2  # Integer division to ensure result is an integer
        
        # Calculate the difference between the triangular number and n
        m = s - n
        
        # Check if the triangular number equals n
        if s == n:
            print(i)  # Output the index
            break
        
        # Check if the triangular number is greater than n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:  # Using modulo to check even
                print(i)  # Output the index
                break
        
        # Increment the index for the next triangular number
        i += 1

# Call the function to execute
find_triangle_number()
