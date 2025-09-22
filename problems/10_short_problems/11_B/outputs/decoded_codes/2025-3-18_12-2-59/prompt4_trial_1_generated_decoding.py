def find_index():
    # Read an integer input and store its absolute value
    number = abs(int(input()))
    index = 0

    # Infinite loop to find the desired index
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_value = (index * (index + 1)) // 2  # Using integer division
        
        # Calculate the difference between the sum and the target number
        difference = sum_value - number
        
        # Check if the sum equals the target number
        if sum_value == number:
            print(index)
            break
        
        # Check if the sum exceeds the target number
        elif sum_value > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next iteration
        index += 1

# Call the function to execute the logic
find_index()
