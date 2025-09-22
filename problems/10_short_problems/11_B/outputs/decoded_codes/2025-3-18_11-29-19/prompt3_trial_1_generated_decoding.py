def find_index():
    # Step 1: Get input from the user and convert it to a positive integer
    user_input = abs(int(input()))
    
    # Step 2: Initialize a variable to keep track of the current index
    index = 0
    
    # Step 3: Start an infinite loop to find the required index
    while True:
        # Step 4: Calculate the sum of the first 'index' integers
        sum_of_integers = (index * (index + 1)) // 2
        
        # Step 5: Calculate the difference between the sum and the user input
        difference = sum_of_integers - user_input
        
        # Step 6: Check if the sum equals the user input
        if sum_of_integers == user_input:
            # Step 7: If equal, print the current index and exit the loop
            print(index)
            break
        
        # Step 8: Check if the sum is greater than the user input
        elif sum_of_integers > user_input:
            
            # Step 9: Check if the difference is an even number
            if difference % 2 == 0:
                # Step 10: If even, print the current index and exit the loop
                print(index)
                break
        
        # Step 11: Increment the index for the next iteration
        index += 1

# Call the function to execute
find_index()
