# Function to find the required index based on user input
def find_index():
    # Step 1: Accept input from the user and convert it to a positive integer
    user_input = input()  # get user input as a string
    number = abs(int(user_input))  # convert to integer and take absolute value

    # Step 2: Initialize a variable to track iterations
    index = 0

    # Step 3: Enter an infinite loop to find the solution
    while True:
        # Calculate the sum of the first `index` numbers
        sum_index = (index * (index + 1)) // 2  # use integer division for sum calculation
        
        # Calculate the difference between sum and the input number
        difference = sum_index - number
        
        # Step 4: Check if the sum is exactly equal to the number
        if sum_index == number:
            print(index)  # Output the current index
            break  # Exit the loop
        
        # Step 5: Check if the sum exceeds the input number
        elif sum_index > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Exit the loop

        # Step 6: Increment the index for the next iteration
        index += 1  # Update the index for the next iteration

# Call the function to execute
find_index()
