# Start the program

# Get input from the user and convert it to a positive integer
target_number = abs(int(input()))

# Initialize a counter to find the smallest non-negative integer
integer = 0

# Start an infinite loop to search for the required integer
while True:
    # Calculate the sum of all integers from 0 to 'integer' (triangular number formula)
    sum_of_integers = (integer * (integer + 1)) // 2
    
    # Calculate the difference from the target number
    difference = sum_of_integers - target_number
    
    # Check if the sum of integers is equal to the target number
    if sum_of_integers == target_number:
        print(integer)  # Print the result and exit the loop
        break
    
    # Check if the sum exceeds the target number
    if sum_of_integers > target_number:
        # If the difference is an even number, print the integer and exit the loop
        if difference % 2 == 0:
            print(integer)  # Print the result and exit the loop
            break
    
    # Increment the integer to check the next number
    integer += 1

# End the program
