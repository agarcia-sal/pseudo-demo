# Step 1: Accept an input value and convert it to its absolute value
input_value = abs(int(input()))
index = 0  # Initialize index

# Step 2: Start an infinite loop to find the correct index
while True:
    # Step 3: Calculate the sum of the first 'index' natural numbers
    sum_of_naturals = (index * (index + 1)) // 2
    
    # Step 4: Calculate the difference between the sum and input value
    difference = sum_of_naturals - input_value
    
    # Step 5: Check if the sum equals the input value
    if sum_of_naturals == input_value:
        # Step 5a: If they are equal, print the current index
        print(index)
        break  # Exit the loop
    
    # Step 6: Check if the sum is greater than the input value
    elif sum_of_naturals > input_value:
        # Step 6a: Check if the difference is even
        if difference % 2 == 0:
            # Step 6b: If the difference is even, print the current index
            print(index)
            break  # Exit the loop
            
    # Step 7: Move to the next index for the next iteration
    index += 1
