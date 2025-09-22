# Step 1: Get the absolute value of an input integer
absolute_value = abs(int(input()))  # Storing the absolute value in absolute_value

# Step 2: Initialize index variable to track the current integer being evaluated
index = 0

# Step 3: Enter an infinite loop to evaluate conditions based on index
while True:
    # Calculate the sum of the first index integers using the formula
    sum_of_integers = index * (index + 1) // 2  # Using integer division for precise calculation
    # Calculate the difference between sum_of_integers and absolute_value
    difference = sum_of_integers - absolute_value

    # Step 4: Check if sum_of_integers is equal to absolute_value
    if sum_of_integers == absolute_value:
        print(index)  # Output the index as the result
        break  # Exit the loop
    
    # Step 5: Check if sum_of_integers is greater than absolute_value
    if sum_of_integers > absolute_value:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)  # Output the index as the result
            break  # Exit the loop
    
    # Step 6: Increase index by 1 to evaluate the next integer
    index += 1
