# Start of the program

# Step 1: Prompt user for input and store the absolute value of the integer
number = abs(int(input()))

# Step 2: Initialize a counter variable
index = 0

# Step 3: Infinite loop to find the solution
while True:
    
    # Step 4: Calculate the sum of the first 'index' integers
    sum_of_integers = (index * (index + 1)) / 2
    
    # Step 5: Calculate the difference between the sum and the input number
    difference = sum_of_integers - number
    
    # Step 6: Check if the sum equals the input number
    if sum_of_integers == number:
        print(index)  # Output the index
        break  # Exit the loop
        
    # Step 7: Check if the sum exceeds the input number
    elif sum_of_integers > number:
        # Step 8: Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the index
            break  # Exit the loop
            
    # Step 9: Increment the counter variable
    index += 1
    
# End of the program
