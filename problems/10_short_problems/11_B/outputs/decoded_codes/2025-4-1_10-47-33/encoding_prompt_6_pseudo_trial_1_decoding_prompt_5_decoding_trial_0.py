# Function to find the maximum integer based on specific conditions
def find_max_integer():
    # Read absolute value of user input and convert it to an integer
    user_input = abs(int(input()))  
    integer_value = user_input
    
    # Initialize an index for iteration
    index = 0

    # Begin an infinite loop to process until we find the solution
    while True:
        # Calculate the sum of the first 'index' integers
        sum_of_integers = (index * (index + 1)) / 2
        
        # Calculate the difference between the current sum and the input value
        difference = sum_of_integers - integer_value

        # Check if the current sum is exactly equal to the input value
        if sum_of_integers == integer_value:
            # If equal, print the current index and exit the loop
            print(index)
            break

        # Check if the current sum is greater than the input value
        elif sum_of_integers > integer_value:
            # Check if the difference is an even number
            if difference % 2 == 0:
                # If the difference is even, print the current index and exit the loop
                print(index)
                break

        # Increment the index for the next iteration
        index += 1

# Example test case
# Uncomment the following line to test the function
# find_max_integer()
