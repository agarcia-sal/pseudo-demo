# Function to find the index where the sum of first index natural numbers equals the target sum
def find_index_for_target_sum():
    # Step 2: Get input and store the absolute value in target_sum
    target_sum = abs(int(input()))
    
    # Step 3: Initialize index to 0
    index = 0
    
    # Step 4: Repeat indefinitely
    while True:
        # Step 4.a: Calculate currentSum using the formula for the sum of first index natural numbers
        current_sum = (index * (index + 1)) / 2
        
        # Step 4.b: Calculate the difference between currentSum and targetSum
        difference = current_sum - target_sum
        
        # Step 4.c: Check if currentSum equals targetSum
        if current_sum == target_sum:
            print(index)  # Print the index
            break  # Exit the loop
        
        # Step 4.d: Check if currentSum is greater than targetSum
        if current_sum > target_sum:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(index)  # Print the index
                break  # Exit the loop
        
        # Step 4.e: Increment index
        index += 1

# Uncomment the following line to run the function
# find_index_for_target_sum()
