def main():
    # Step 2: Input the integer value and take its absolute value
    target_number = abs(int(input()))
    
    # Step 3: Initialize the index
    index = 0

    # Step 4: Begin an infinite loop
    while True:
        # Calculate the current sum using the formula for the sum of the first 'index' natural numbers
        current_sum = index * (index + 1) // 2
        
        # Calculate the difference
        difference = current_sum - target_number
        
        # Step 5: Conditions
        if current_sum == target_number:
            print(index)
            break  # Exit the loop if current sum equals target number
        elif current_sum > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop if the difference is even
        
        # Step 6: Update
        index += 1  # Increment the index

# Entry point of the program
if __name__ == "__main__":
    main()
