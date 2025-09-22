def main():
    # Step 1: Read an integer input and store its absolute value
    target_sum = abs(int(input()))
    
    # Step 2: Initialize a counter for the current index
    current_index = 0
    
    while True:  # Step 3: Start an infinite loop to find the target sum
        # Step 4: Calculate the sum of the first 'current_index' integers
        sum_of_series = (current_index * (current_index + 1)) // 2
        
        # Step 5: Calculate the difference with the target sum
        difference = sum_of_series - target_sum
        
        # Step 6: Check conditions for valid output
        if sum_of_series == target_sum:
            print(current_index)  # Exact match found
            break
        elif sum_of_series > target_sum:
            if difference % 2 == 0:  # Check if difference is even
                print(current_index)  # Valid output found
                break
        
        # Step 7: Increment the counter
        current_index += 1

if __name__ == "__main__":
    main()
