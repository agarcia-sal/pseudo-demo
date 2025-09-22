# Function to find the smallest integer i such that the sum of the first i integers
# is equal to or exceeds the given positive integer n.
def find_smallest_integer():
    # Step 1: Get Input
    target_number = abs(int(input()))  # Read the absolute value of the input number

    # Step 2: Initialize Counter
    counter = 0  # Counter to keep track of the current integer

    # Step 3: Start Infinite Loop
    while True:
        # Step 3a: Calculate Sum
        current_sum = (counter * (counter + 1)) // 2  # Sum of the first 'counter' integers

        # Step 3b: Calculate Difference
        difference = current_sum - target_number  # Difference between current sum and target number

        # Step 3c: Check for Matching Sum
        if current_sum == target_number:
            print(counter)  # Print the value of 'counter'
            break  # Exit the loop
        
        # Step 3d: Check for Exceeding Sum
        if current_sum > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(counter)  # Print the value of 'counter'
                break  # Exit the loop

        # Step 3e: Increment Counter
        counter += 1  # Increase the value of 'counter' by 1

# Execute the function to find the smallest integer
find_smallest_integer()
