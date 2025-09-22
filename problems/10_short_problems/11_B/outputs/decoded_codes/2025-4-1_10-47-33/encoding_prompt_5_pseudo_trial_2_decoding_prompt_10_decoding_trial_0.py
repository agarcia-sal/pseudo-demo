def find_index_with_target_sum():
    # Step 2: Input the Number
    target_sum = abs(int(input()))
    
    # Step 3: Initialize Counter
    index = 0

    # Step 4: Begin Infinite Loop
    while True:
        # Step 4a: Calculate the Sum of the First 'index' Integers
        current_sum = (index * (index + 1)) // 2

        # Step 4b: Calculate the Difference
        difference = current_sum - target_sum

        # Step 4c: Check for Equality
        if current_sum == target_sum:
            print(index)
            break

        # Step 4d: Check for Exceeding the Target
        if current_sum > target_sum:
            if difference % 2 == 0:
                print(index)
                break

        # Step 4e: Increment the Counter
        index += 1

# Example function call to run the program
find_index_with_target_sum()
