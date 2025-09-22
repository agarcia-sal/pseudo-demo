# Start of the program

# Step 2: Input an integer value and take its absolute value
input_value = abs(int(input()))

# Step 3: Initialize a variable to 0
current_integer = 0

# Step 4: Loop continuously to find the minimum integer
while True:
    # Calculate the sum of the first 'current_integer' integers
    sum_of_integers = (current_integer * (current_integer + 1)) / 2
    
    # Calculate the difference between the sum and the input value
    difference = sum_of_integers - input_value

    # Check the conditions for printing the result
    if sum_of_integers == input_value:
        # If the sum is exactly equal to the input value
        print(current_integer)
        break
    elif sum_of_integers > input_value:
        # If the sum exceeds the input value
        if difference % 2 == 0:
            # If the difference is an even number
            print(current_integer)
            break

    # Step 6: Increment the value of current_integer to check the next integer
    current_integer += 1

# End of the program
