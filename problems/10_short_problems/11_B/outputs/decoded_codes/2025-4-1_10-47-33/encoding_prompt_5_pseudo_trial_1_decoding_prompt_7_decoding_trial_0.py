# Start the program

# Step 2: Read an integer input from the user and take its absolute value
userInput = abs(int(input()))

# Step 3: Initialize a variable index to 0
index = 0

# Step 4: Create an infinite loop to continue examining integers
while True:
    # Calculate the sum of the first 'index' integers using the formula for sum of first n integers
    sum = (index * (index + 1)) // 2  # Using integer division for clarity

    # Calculate the difference
    difference = sum - userInput

    # Step 5: Check if the sum equals userInput
    if sum == userInput:
        print(index)  # Print index as the solution
        break  # End the program

    # Step 6: Otherwise, check if the sum is greater than userInput
    elif sum > userInput:
        # If it is, check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print index as the solution
            break  # End the program

    # Step 7: Increment the index by 1 to check the next integer
    index += 1
