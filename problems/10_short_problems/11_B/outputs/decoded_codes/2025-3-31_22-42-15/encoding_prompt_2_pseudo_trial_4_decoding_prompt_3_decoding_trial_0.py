def find_matching_index():
    # Step 2: Read an integer value from the user and take its absolute value
    target_number = abs(int(input()))
    
    # Step 3: Initialize index
    index = 0

    # Step 4: Begin an infinite loop
    while True:
        # Calculate the sum of the first 'index' natural numbers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference
        difference = current_sum - target_number

        # Step 5: Evaluate conditions
        if current_sum == target_number:
            # If currentSum equals targetNumber, print index and exit
            print(index)
            break
        
        elif current_sum > target_number:
            # If currentSum is greater than targetNumber
            if difference % 2 == 0:
                # Check if difference is an even number
                print(index)
                break
        
        # Step 6: Increment index
        index += 1

# Call the function to execute
find_matching_index()
