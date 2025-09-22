# Step 1: Read an integer input from the user and store its absolute value in 'distanceFromSum'.
distanceFromSum = abs(int(input()))

# Step 2: Initialize a variable 'index' to zero.
index = 0

# Step 3: Start an infinite loop.
while True:
    # Step 3a: Calculate the sum of the first 'index' natural numbers.
    sumOfFirstN = (index * (index + 1)) / 2
    
    # Step 3b: Calculate the difference from target.
    differenceFromTarget = sumOfFirstN - distanceFromSum
    
    # Step 3c: Check if sumOfFirstN is equal to distanceFromSum.
    if sumOfFirstN == distanceFromSum:
        print(index)  # Print 'index'.
        break  # Exit the loop.
    
    # Step 3d: Check if sumOfFirstN is greater than distanceFromSum.
    if sumOfFirstN > distanceFromSum:
        # Check if differenceFromTarget is an even number.
        if differenceFromTarget % 2 == 0:
            print(index)  # Print 'index'.
            break  # Exit the loop.
    
    # Step 3e: Increment 'index' by 1.
    index += 1
