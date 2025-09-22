# Step 1: Get user input
inputNumber = abs(int(input()))

# Step 2: Initialize loop variable
index = 0

# Step 3: Begin an infinite loop to find the solution
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum = (index * (index + 1)) // 2
    
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


def find_index(inputNumber):
    inputNumber = abs(inputNumber)
    index = 0
    
    while True:
        sum = (index * (index + 1)) // 2
        difference = sum - inputNumber

        if sum == inputNumber or (sum > inputNumber and difference % 2 == 0):
            return index
        
        index += 1
