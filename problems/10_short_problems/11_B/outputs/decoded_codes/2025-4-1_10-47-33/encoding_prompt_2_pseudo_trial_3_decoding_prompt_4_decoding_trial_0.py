def main():
    # Step 1: Receive an integer input, take its absolute value
    target_number = abs(int(input()))
    
    # Step 2: Initialize the currentIndex to 0
    current_index = 0

    # Step 3: Enter an infinite loop to perform calculations
    while True:
        # Step 4a: Calculate the sum of integers from 0 to currentIndex
        sum_value = (current_index * (current_index + 1)) // 2
        
        # Step 4b: Determine the difference from the target
        difference_from_target = sum_value - target_number
        
        # Step 4c: Check if sum_value equals target_number
        if sum_value == target_number:
            print(current_index)
            break  # Exit the loop if the condition is met
        
        # Step 4d: If sum_value is greater than target_number
        if sum_value > target_number:
            # Check if the difference is even
            if difference_from_target % 2 == 0:
                print(current_index)
                break  # Exit the loop if the condition is met
        
        # Step 4e: Increment currentIndex for the next iteration
        current_index += 1

# Step 5: Run the main function to execute the program
if __name__ == "__main__":
    main()
