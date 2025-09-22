# Function to find the smallest integer i such that
# the sum of the first i integers either equals
# or can be adjusted to equal a user-provided absolute integer n
def find_integer_equal_to_sum():
    # Input the absolute value of an integer
    n = abs(int(input()))
    
    # Initialize index variable
    i = 0
    
    # Loop indefinitely
    while True:
        # Calculate the sum of the first i integers using the formula
        sum_of_integers = (i * (i + 1)) // 2
        
        # Calculate the difference between the sum and n
        difference = sum_of_integers - n
        
        # Check if the sum equals n
        if sum_of_integers == n:
            print(i)
            break  # Exit the loop
        
        # Check if the sum is greater than n
        if sum_of_integers > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(i)
                break  # Exit the loop
        
        # Increment the index variable
        i += 1

# Call the function
find_integer_equal_to_sum()
