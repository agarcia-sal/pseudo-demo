# Step 1: Read an integer input from the user
userInput = abs(int(input()))
index = 0

# Step 2: Infinite loop to find the required index
while True:
    
    # Calculate the sum of the first 'index' natural numbers
    sum_value = (index * (index + 1)) // 2
    
    # Calculate the difference from the user input
    difference = sum_value - userInput
    
    # Step 3: Check if we found the desired sum
    if sum_value == userInput:
        print(index)
        break
        
    # Step 4: If sum is greater than user input
    elif sum_value > userInput:
        
        # Step 5: Check if the difference is even
        if difference % 2 == 0:
            print(index)
            break
            
    # Step 6: Increment index for the next iteration
    index += 1
