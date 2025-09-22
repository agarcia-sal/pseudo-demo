# Step 1: Define a variable `number` as the absolute value of an integer input from the user.
number = abs(int(input()))

# Step 2: Initialize a variable `index` to zero
index = 0

# Step 3: Start an infinite loop
while True:
    # Step 4: Calculate the sum `sumValue` of the first `index` natural numbers
    sumValue = index * (index + 1) // 2  # Using the formula for the sum of the first `index` natural numbers
    
    # Step 5: Determine the difference `difference` between `sumValue` and `number`
    difference = sumValue - number
    
    # Step 6: Check if `sumValue` is equal to `number`
    if sumValue == number:
        print(index)  # Print `index` as the result
        break  # Exit the loop
        
    # Step 7: If `sumValue` is greater than `number`, check if `difference` is an even number
    if sumValue > number:
        if difference % 2 == 0:  # Check if the `difference` is even
            print(index)  # Print `index` as the result
            break  # Exit the loop
            
    # Step 8: If neither condition is met, increment `index` by one
    index += 1
