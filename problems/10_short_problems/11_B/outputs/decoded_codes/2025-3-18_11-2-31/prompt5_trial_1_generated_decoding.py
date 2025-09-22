# The program finds a non-negative integer where the sum of the first 'i' integers
# either matches the absolute input number or results in an even difference.

# Step 1: Get the absolute value of an integer input from the user
absolute_number = abs(int(input()))

# Step 2: Initialize a counter for numbers
counter = 0

# Step 3: Start an indefinite loop to find the desired number
while True:
    # Calculate the sum of the first 'counter' integers
    sum_of_integers = (counter * (counter + 1)) // 2

    # Calculate the difference between sum and absolute_number
    difference = sum_of_integers - absolute_number
    
    # Check if the calculated sum equals the absolute number
    if sum_of_integers == absolute_number:
        # If they are equal, print the counter and exit the loop
        print(counter)
        break
    
    # Check if the calculated sum is greater than the absolute number
    elif sum_of_integers > absolute_number:
        # Check if the difference is even
        if difference % 2 == 0:
            # If the difference is even, print the counter and exit the loop
            print(counter)
            break

    # Increment the counter for the next iteration
    counter += 1
