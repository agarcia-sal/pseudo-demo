# This program finds a non-negative integer index such that the sum of the first 'index' natural numbers 
# satisfies a specific mathematical condition related to an input value provided by the user.

# Step 1: Accept an input value from the user
input_value = abs(int(input()))

# Initialize index to iterate through natural numbers
index = 0

# Step 2: Start an infinite loop to find the correct index
while True:
    # Step 3: Calculate the sum of the first 'index' natural numbers
    sum_value = (index * (index + 1)) // 2  # Using integer division for precision
    
    # Step 4: Calculate the difference between the sum and the input value
    difference = sum_value - input_value
    
    # Step 5: Check if the sum equals the input value
    if sum_value == input_value:
        print(index)  # Step 5a: Print the current index if they are equal
        break  # Exit the loop
    
    # Step 6: Check if the sum is greater than the input value
    elif sum_value > input_value:
        # Step 6a: Check if the difference is even
        if difference % 2 == 0:  # Using modulo operator to check evenness
            # Step 6b: If the difference is even, print the current index
            print(index)
            break  # Exit the loop

    # Step 7: Move to the next index for the next iteration
    index += 1
