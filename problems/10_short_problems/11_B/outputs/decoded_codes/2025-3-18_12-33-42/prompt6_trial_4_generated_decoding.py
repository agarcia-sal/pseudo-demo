# Begin the execution of the program

# Read an integer input and take its absolute value
target_number = abs(int(input()))

# Initialize the index variable used for calculations
index = 0

# Infinite loop to explore values of index
while True:
    # Calculate the sum of the first 'index' integers
    sum_of_integers = (index * (index + 1)) / 2
    
    # Calculate the difference between the sum and the target number
    difference = sum_of_integers - target_number

    # Check if the calculated sum equals the target number
    if sum_of_integers == target_number:
        # Print the index if the sum matches the target number
        print(index)
        break  # Exit the loop

    # Check if the calculated sum exceeds the target number
    elif sum_of_integers > target_number:
        # Check if the difference is even
        if difference % 2 == 0:
            # Print the index if the difference is even
            print(index)
            break  # Exit the loop
    
    # Increment the index for the next iteration
    index += 1

# End of the program
