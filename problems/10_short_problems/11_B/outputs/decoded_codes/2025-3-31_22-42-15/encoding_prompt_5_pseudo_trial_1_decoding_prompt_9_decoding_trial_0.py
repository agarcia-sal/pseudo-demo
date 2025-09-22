# Start of the program
input_value = abs(int(input()))  # Step 1: Accept an input value and take absolute value
index = 0  # Step 1: Initialize index

# Step 2: Start an infinite loop to find the correct index
while True:
    # Step 3: Calculate the sum of the first 'index' natural numbers
    sum_of_numbers = (index * (index + 1)) // 2  # Using integer division for clarity
    
    # Step 4: Calculate the difference between the sum and input value
    difference = sum_of_numbers - input_value
    
    # Step 5: Check if the sum equals the input value
    if sum_of_numbers == input_value:
        print(index)  # Step 5a: Print the current index
        break  # Exit the loop
    
    # Step 6: Check if the sum is greater than the input value
    elif sum_of_numbers > input_value:
        # Step 6a: Check if the difference is even
        if difference % 2 == 0:
            # Step 6b: Print the current index if the difference is even
            print(index)
            break  # Exit the loop
    
    # Step 7: Move to the next index for the next iteration
    index += 1  # Increment the index
