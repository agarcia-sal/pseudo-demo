def find_index_for_target_value():
    # Step 1: Get the absolute value of the user input
    user_input = int(input())
    target_value = abs(user_input)

    # Step 2: Initialize a counter variable
    index = 0

    # Step 3: Start an infinite loop to find the required index
    while True:
        # Step 4: Calculate the sum of the first 'index' integers
        sum_of_integers = (index * (index + 1)) // 2

        # Step 5: Calculate the difference from the target value
        difference = sum_of_integers - target_value

        # Step 6: Check if the current sum equals the target value
        if sum_of_integers == target_value:
            print(index)
            break   # Exit the loop if we found a match

        # Step 7: Check if the current sum exceeds the target value
        elif sum_of_integers > target_value:
            # Step 8: Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break   # Exit the loop if the difference is even

        # Step 9: Increment the index for the next iteration
        index += 1

# To execute the function
find_index_for_target_value()
