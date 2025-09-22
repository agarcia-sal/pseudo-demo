# Begin algorithm to find the smallest non-negative integer i 
# such that the sum of the first i integers equals n or is larger than n 
# and the difference is even.

# Get absolute value of input as a non-negative integer
input_value = abs(int(input()))  # Input must be treated as an integer
index = 0  # Initialize index i to zero

# Start an infinite loop to find the required integer
while True:
    # Calculate the sum of the first index integers
    sum_of_integers = (index * (index + 1)) / 2
    
    # Calculate the difference between the sum and the target input value
    difference = sum_of_integers - input_value
    
    # Check if the sum equals the input value
    if sum_of_integers == input_value:
        # If it matches, print the current index and exit
        print(index)
        break  # Exit the loop
    
    # Check if the sum exceeds the input value
    elif sum_of_integers > input_value:
        # Check if the difference is even
        if difference % 2 == 0:  # 'is even' condition 
            # If the difference is even, print the current index and exit
            print(index)
            break  # Exit the loop
            
    # Increment the index for the next iteration
    index += 1  # Move to the next integer
