# Function to find the first non-negative integer satisfying the required condition
def find_non_negative_integer():
    # Step 1: Get input integer 'n' from the user
    n = abs(int(input()))  # Ensure 'n' is an absolute positive integer

    # Step 2: Initialize index
    index = 0
    
    # Step 3: Infinite loop to find the solution
    while True:
        # Step 4: Calculate the sum of the first 'index' integers
        sum_up_to_index = (index * (index + 1)) // 2
        
        # Step 5: Calculate the difference
        difference = sum_up_to_index - n
        
        # Step 6: Check if the sum matches 'n'
        if sum_up_to_index == n:
            print(index)  # Output the current index
            break  # Exit the loop
        
        # Step 7: Check if the sum is greater than 'n'
        if sum_up_to_index > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index and exit
                break
        
        # Step 8: Increment the index
        index += 1

# Example of how you would call the function
# find_non_negative_integer()  # Uncomment this line to run the function
