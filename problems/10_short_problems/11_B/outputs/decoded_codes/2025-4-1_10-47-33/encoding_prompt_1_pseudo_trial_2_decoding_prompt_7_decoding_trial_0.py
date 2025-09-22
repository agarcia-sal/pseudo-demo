# Function to calculate the maximum integer for a given condition
def calculate_max_integer():
    # 1. Input Handling: Read a number from the user and store its absolute value
    absolute_input = abs(int(input()))

    # 2. Initialize a Counter
    index = 0  # Counter to track the current integer

    # 3. Infinite Loop for Calculation
    while True:
        # Calculate the sum of the first `index` integers
        current_sum = (index * (index + 1)) // 2  # Integer division to avoid float

        # Calculate the difference between current_sum and absolute_input
        difference = current_sum - absolute_input
        
        # 3.1 Check Conditions
        if current_sum == absolute_input:
            print(index)  # Output the index if current_sum equals absolute_input
            break  # Exit the loop
        
        if current_sum > absolute_input:
            # 3.2 If current_sum is greater than absolute_input
            if difference % 2 == 0:  # Check if difference is an even number
                print(index)  # Output the index
                break  # Exit the loop

        # 4. Increment the Counter
        index += 1  # Move to the next integer

# Call the function to execute the logic
calculate_max_integer()
