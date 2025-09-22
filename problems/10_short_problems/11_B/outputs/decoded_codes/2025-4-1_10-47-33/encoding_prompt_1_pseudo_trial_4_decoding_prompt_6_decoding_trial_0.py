# Begin the program
# Get an input value from the user and convert it to an absolute integer
input_number = abs(int(input()))

# Initialize a counter variable 'index' to 0
index = 0

# Start an infinite loop
while True:
    # Calculate the sum of all integers from 0 to 'index' using the formula
    sum_of_integers = (index * (index + 1)) // 2
    
    # Calculate 'difference' by subtracting 'input_number' from 'sum_of_integers'
    difference = sum_of_integers - input_number
    
    # Check if 'sum_of_integers' is equal to 'input_number'
    if sum_of_integers == input_number:
        print(index)  # Print the value of 'index' and exit the loop
        break  # Exit the loop
    
    # Otherwise, if 'sum_of_integers' is greater than 'input_number'
    elif sum_of_integers > input_number:
        # Check if 'difference' is an even number
        if difference % 2 == 0:
            print(index)  # Print the value of 'index' and exit the loop
            break  # Exit the loop
            
    # Increment 'index' by 1
    index += 1

# End the program
