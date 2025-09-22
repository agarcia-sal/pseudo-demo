# START

# Step 1: Get user input
inputNumber = abs(int(input()))

# Step 2: Initialize loop variable
index = 0

# Step 3: Begin an infinite loop to find the solution
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum = (index * (index + 1)) // 2  # Using integer division
    
    # Calculate the difference between the sum and inputNumber
    difference = sum - inputNumber

    # Step 4: Check if the current sum equals the input number
    if sum == inputNumber:
        print(index)
        break

    # Step 5: Check if the current sum exceeds the input number
    elif sum > inputNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)
            break
            
    # Increment the loop variable
    index += 1

# END
