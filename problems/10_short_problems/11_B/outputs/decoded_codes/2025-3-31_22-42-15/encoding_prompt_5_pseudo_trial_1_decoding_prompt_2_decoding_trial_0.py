# Step 1: Accept an input value
inputValue = abs(int(input()))  # Converting input to absolute value
index = 0

# Step 2: Start an infinite loop to find the correct index
while True:
    
    # Step 3: Calculate the sum of the first 'index' natural numbers
    sum = (index * (index + 1)) // 2  # Use integer division

    # Step 4: Calculate the difference between the sum and input value
    difference = sum - inputValue

    # Step 5: Check if the sum equals the input value
    if sum == inputValue:
        # Step 5a: If they are equal, print the current index
        print(index)
        break

    # Step 6: Check if the sum is greater than the input value
    elif sum > inputValue:
        
        # Step 6a: Check if the difference is even
        if difference % 2 == 0:
            # Step 6b: If the difference is even, print the current index
            print(index)
            break
            
    # Step 7: Move to the next index for the next iteration
    index += 1
