# Start the program.
number = abs(int(input()))  # Read an integer input value and store its absolute value in a variable `number`.
index = 0  # Initialize a counter variable `index` to 0.

# Begin an infinite loop:
while True:
    # a. Calculate the sum of the first `index` natural numbers
    sum_of_first_index = (index * (index + 1)) // 2  # Use integer division
    
    # b. Calculate the difference between `sum_of_first_index` and `number`
    difference = sum_of_first_index - number
    
    # c. Check if `sum_of_first_index` is equal to `number`
    if sum_of_first_index == number:
        print(index)  # If true, print the value of `index` and exit the loop.
        break
    
    # d. Else, check if `sum_of_first_index` is greater than `number`
    elif sum_of_first_index > number:
        # If true, check if `difference` is even
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # If true, print the value of `index` and exit the loop.
            break
    
    # e. Increment `index` by 1.
    index += 1

# End the program.
