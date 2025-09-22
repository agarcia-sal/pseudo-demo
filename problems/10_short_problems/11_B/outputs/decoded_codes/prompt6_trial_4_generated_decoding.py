# Step 1: Read the absolute value of an integer input
number = abs(int(input()))  # Taking the absolute value of the input integer

# Step 2: Initialize the index variable
index = 0

# Step 3: Start an infinite loop to find a suitable index
while True:
    
    # Step 4: Calculate the sum of the first 'index' integers (triangular number)
    triangular_sum = (index * (index + 1)) // 2  # Use integer division

    # Step 5: Calculate the difference between the sum and the input number
    difference = triangular_sum - number

    # Step 6: Check if the sum equals the input number
    if triangular_sum == number:
        print(index)  # Output the current index
        break  # Exit the loop
    
    # Step 7: Check if the sum exceeds the input number
    elif triangular_sum > number:
        
        # Step 8: Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the current index
            break  # Exit the loop
    
    # Step 9: Increment the index variable for the next iteration
    index += 1
