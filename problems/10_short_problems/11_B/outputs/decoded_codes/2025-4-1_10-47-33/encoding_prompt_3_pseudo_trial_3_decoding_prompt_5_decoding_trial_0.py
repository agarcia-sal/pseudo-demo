# Function to find the index where the sum of the first 'index' natural numbers 
# either equals or differs from a target value in an acceptable way
def find_index_for_target_value():
    # Step 1: Get the absolute value of input and convert it to an integer
    target_value = abs(int(input()))
    
    # Step 2: Initialize counter variable
    index = 0
    
    # Step 3: Start an infinite loop to find the value
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_of_naturals = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and target_value
        difference = sum_of_naturals - target_value
        
        # Step 4: Check if the sum matches the target_value
        if sum_of_naturals == target_value:
            print(index)  # Output the current index and exit the loop
            break
        
        # Step 5: Check if the sum exceeds the target_value
        elif sum_of_naturals > target_value:
            # Step 6: Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index and exit the loop
                break
        
        # Increment the index for the next iteration
        index += 1

# Uncomment the line below to run the function
# find_index_for_target_value()
