# Step 1: Get user input and convert to absolute integer
integer_value = abs(int(input()))

# Step 2: Initialize a counter variable
index = 0

# Step 3: Create an infinite loop to find a solution
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_of_natural_numbers = (index * (index + 1)) // 2
    
    # Calculate the difference between the calculated sum and the input value
    difference = sum_of_natural_numbers - integer_value
    
    # Step 4: Check if the calculated sum matches the input value
    if sum_of_natural_numbers == integer_value:
        # If they are equal, print the current index and exit the loop
        print(index)
        break
    
    # Step 5: Check if the calculated sum exceeds the input value
    elif sum_of_natural_numbers > integer_value:
        # Check if the difference is even
        if difference % 2 == 0:
            # If the difference is even, print the current index and exit the loop
            print(index)
            break
    
    # Increment the index for the next iteration
    index += 1
