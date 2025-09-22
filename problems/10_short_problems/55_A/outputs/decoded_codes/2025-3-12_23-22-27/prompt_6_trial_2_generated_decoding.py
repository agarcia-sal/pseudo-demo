# Start the program

# Get an integer input called num
num = int(input())

# Create a list called boolean_list initialized with True values of size num
boolean_list = [True] * num

# Initialize an index variable called curr to 0
curr = 0

# Initialize a step variable called step to 1
step = 1

# While step is less than or equal to 500000
while step <= 500000:
    # If the value at boolean_list[curr] is True
    if boolean_list[curr]:
        # Mark this index as processed by setting it to False
        boolean_list[curr] = False
    
    # Increment step by 1
    step += 1
    
    # Update curr as (curr + step) % num to wrap around
    curr = (curr + step) % num

# Create a new list called rem containing all values in boolean_list that are still True
rem = [value for value in boolean_list if value]

# If the size of rem is zero
if len(rem) == 0:
    # Output 'YES' indicating all indices have been marked
    print('YES')
else:
    # Output 'NO' indicating some indices are still unmarked
    print('NO')

# End the program
