# Step 1: Start the program

# Step 2: Prompt the user to enter a number and store this number as inputNumber
inputNumber = int(input())

# Step 3: Calculate the absolute value of inputNumber and assign it to targetValue
targetValue = abs(inputNumber)

# Step 4: Initialize a variable index to 0
index = 0

# Step 5: Enter an infinite loop
while True:
    # Calculate the sum of the first index natural numbers
    sumValue = index * (index + 1) // 2  # using the formula for the sum of the first n natural numbers
    
    # Determine the difference between sumValue and targetValue
    difference = sumValue - targetValue
    
    # If sumValue is equal to targetValue
    if sumValue == targetValue:
        # Output the value of index to the user
        print(index)
        # Exit the loop
        break
    # Else if sumValue is greater than targetValue
    elif sumValue > targetValue:
        # Check if difference is an even number
        if difference % 2 == 0:
            # If true, output the value of index to the user
            print(index)
            # Exit the loop
            break
    
    # Increment index by 1
    index += 1

# Step 6: End the program (implicitly ends when the program flow completes)
