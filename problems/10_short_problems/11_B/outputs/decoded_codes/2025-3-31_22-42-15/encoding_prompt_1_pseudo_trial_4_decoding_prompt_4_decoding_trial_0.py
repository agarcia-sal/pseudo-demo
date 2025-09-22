# Start of the program
# Read an integer input value and store its absolute value in a variable `number`
number = abs(int(input()))

# Initialize a counter variable `index` to 0
index = 0

# Begin an infinite loop
while True:
    # Calculate the sum of the first `index` natural numbers
    sum_of_first_index = (index * (index + 1)) / 2
    
    # Calculate the difference between `sum_of_first_index` and `number`
    difference = sum_of_first_index - number
    
    # Check if `sum_of_first_index` is equal to `number`
    if sum_of_first_index == number:
        print(index)
        break  # Exit the loop
    
    # Check if `sum_of_first_index` is greater than `number`
    elif sum_of_first_index > number:
        # Check if `difference` is even
        if difference % 2 == 0:
            print(index)
            break  # Exit the loop
    
    # Increment `index` by 1
    index += 1

# End of the program
