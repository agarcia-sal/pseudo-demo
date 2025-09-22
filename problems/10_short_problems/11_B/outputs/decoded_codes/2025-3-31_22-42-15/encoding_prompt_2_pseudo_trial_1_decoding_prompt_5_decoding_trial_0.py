# Function to find the index for which the sum of the first index natural numbers meets the target number or certain conditions
def find_target_index():
    # Step 1: Get a number from the user and store its absolute value
    target_number = abs(int(input()))
    
    # Step 2: Initialize a counter variable
    index = 0

    # Step 3: Start an infinite loop
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_of_first_index = (index * (index + 1)) // 2
        
        # Calculate the difference from the target number
        difference = sum_of_first_index - target_number
        
        # Step 4: Check if the current sum equals the target number
        if sum_of_first_index == target_number:
            print(index)
            break

        # Step 5: Check if the current sum exceeds the target number
        if sum_of_first_index > target_number:
            # If difference is even, print the index and exit
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 6: Increment the counter variable
        index += 1

# Example test case (uncomment to run)
# Call the function
# find_target_index()
