# Step 1: Obtain input and convert to absolute integer
userNumber = int(input())
absoluteValue = abs(userNumber)

# Step 2: Initialize counter
counter = 0

# Step 3: Loop to find the required integer
while True:
    # Step 3a: Calculate the sum of the first 'counter' numbers
    sum_of_numbers = (counter * (counter + 1)) // 2
    
    # Step 3b: Calculate the difference between sum and input number
    difference = sum_of_numbers - absoluteValue
    
    # Step 3c: Check if sum matches or exceeds input
    if sum_of_numbers == absoluteValue:
        print(counter)
        break  # Exit loop
    elif sum_of_numbers > absoluteValue:
        # Step 3c.i: Check if the difference is even
        if difference % 2 == 0:
            print(counter)
            break  # Exit loop
    
    # Step 4: Increment counter for next iteration
    counter += 1
