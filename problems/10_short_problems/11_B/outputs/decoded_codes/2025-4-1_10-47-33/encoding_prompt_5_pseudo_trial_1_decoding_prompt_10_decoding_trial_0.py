def find_integer():
    # 2. Read an integer input and set it to be the absolute value
    user_input = abs(int(input()))
    
    index = 0  # 3. Initialize a variable index to 0
    
    # 4. Create an infinite loop to continue examining integers
    while True:
        # Calculate the sum of the first 'index' integers
        # 5. Let sum = (index * (index + 1)) / 2
        current_sum = (index * (index + 1)) // 2  # Use integer division for efficiency
        
        # 6. Calculate a difference value
        difference = current_sum - user_input
        
        # 7. Check if the sum equals userInput
        if current_sum == user_input:
            print(index)
            return  # End the function

        # 8. Check if the sum is greater than userInput
        if current_sum > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                return  # End the function
        
        # 9. Increment the index by 1 to check the next integer
        index += 1

# Call the function to find the integer
find_integer()
