# Function to find a certain triangular number based on user input
def find_triangular_number():
    # Assume n is a non-negative integer input by the user
    n = abs(int(input()))  # Read and take the absolute value of the input as n
    
    # Initialize variable i to count the iterations
    i = 0
    
    # Start an infinite loop to calculate triangular numbers
    while True:
        # Calculate the i-th triangular number
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between the triangular number and n
        m = s - n
        
        # Check if the triangular number is equal to n
        if s == n:
            print(i)  # Output the value of i
            break  # Exit the loop
        
        # Check if the triangular number exceeds n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Output the value of i
                break  # Exit the loop
        
        # Increment i for the next iteration
        i += 1

# Example test cases can be handled by calling the function, 
# but since we don't take any parameters or print instructions, they are not included here.
