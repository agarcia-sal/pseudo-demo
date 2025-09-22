# Function to determine the smallest integer based on given criteria
def find_smallest_integer():
    # Step 1: Take integer input and calculate its absolute value
    absolute_value = abs(int(input()))
    
    # Step 2: Initialize the index variable
    index = 0
    
    # Step 3: Start an infinite loop to evaluate conditions
    while True:
        # Calculate the sum of the first 'index' integers
        sum_of_integers = index * (index + 1) // 2
        
        # Calculate the difference between the sum and absolute value
        difference = sum_of_integers - absolute_value
        
        # Step 4: Check if sum_of_integers is equal to absolute_value
        if sum_of_integers == absolute_value:
            print(index)  # Condition satisfied, print index and exit
            break
        
        # Step 5: If sum_of_integers is greater than absolute_value
        if sum_of_integers > absolute_value:
            # Check if difference is even
            if difference % 2 == 0:
                print(index)  # Condition satisfied, print index and exit
                break
        
        # Step 6: Increment index to check the next integer
        index += 1

# Call the function
find_smallest_integer()
