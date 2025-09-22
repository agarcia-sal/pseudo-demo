def main():
    # Step 1: Receive an integer input from the user and take its absolute value.
    target_number = abs(int(input()))  # Convert the input to integer and take absolute value.
    
    # Step 2: Initialize a counter variable.
    current_index = 0
    
    # Step 3: Infinite loop to find the required index.
    while True:
        # Step 4a: Calculate the sum of integers from 0 to current_index.
        sum_value = (current_index * (current_index + 1)) // 2  # Using integer division
        
        # Step 4b: Determine the difference from the target number.
        difference_from_target = sum_value - target_number
        
        # Step 4c: Check if sum_value is equal to target_number.
        if sum_value == target_number:
            print(current_index)  # Print currentIndex and exit the loop.
            break
        
        # Step 4d: If sum_value is greater than target_number, check if the difference is even.
        if sum_value > target_number and difference_from_target % 2 == 0:
            print(current_index)  # Print currentIndex and exit the loop.
            break
        
        # Step 4e: Increment current_index by 1.
        current_index += 1

# Execute the main function to run the program.
main()
