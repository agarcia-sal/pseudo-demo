def find_suitable_integer():
    # Read and convert the user input to an absolute integer
    user_input = abs(int(input()))
    index = 0

    # Start an infinite loop to find the suitable integer
    while True:
        # Calculate the sum of the first 'index' natural numbers
        total_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the user input
        difference = total_sum - user_input
        
        # Check if the calculated sum equals the user input
        if total_sum == user_input:
            print(index)  # Print the index if found
            break  # Exit the loop
        # Check if the calculated sum is greater than the user input
        elif total_sum > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the index if found
                break  # Exit the loop
        
        # Increment the index for the next iteration
        index += 1

# Example test case (uncomment to test)
# You can provide input values here for testing, such as:
# Input: 5 should ideally print 3 since sum(0, 1, 2, 3) = 6, and 6 - 5 = 1 (odd)
# Input: 3 should print 2 as sum(0, 1, 2) = 3
