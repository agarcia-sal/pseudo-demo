def find_index():
    # Step 1: Read an integer input from the user
    userInput = abs(int(input()))
    index = 0

    # Step 2: Infinite loop to find the required index
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_natural = (index * (index + 1)) // 2
        
        # Calculate the difference from the user input
        difference = sum_natural - userInput
        
        # Step 3: Check if we found the desired sum
        if sum_natural == userInput:
            print(index)
            break
            
        # Step 4: If sum is greater than user input
        elif sum_natural > userInput:
            # Step 5: Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 6: Increment index for the next iteration
        index += 1

# To call the function:
find_index()
