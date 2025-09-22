# START

# Step 1: Get input from the user
userInput = abs(int(input()))

# Step 2: Initialize the variable for iteration
index = 0

# Step 3: Begin an infinite loop to search for the solution
while True:

    # Step 4: Calculate the sum of the first 'index' natural numbers
    sum = (index * (index + 1)) // 2

    # Step 5: Calculate the difference between the sum and the user input
    difference = sum - userInput

    # Step 6: Check if the sum equals the user input
    if sum == userInput:
        # Step 6a: Print the current index
        print(index)
        # Step 6b: Exit the loop
        break

    # Step 7: Check if the sum exceeds the user input
    elif sum > userInput:
        # Step 7a: Check if the difference is even
        if difference % 2 == 0:
            # Step 7b: Print the current index
            print(index)
            # Step 7c: Exit the loop
            break

    # Step 8: Increment the index for the next iteration
    index += 1

# END
