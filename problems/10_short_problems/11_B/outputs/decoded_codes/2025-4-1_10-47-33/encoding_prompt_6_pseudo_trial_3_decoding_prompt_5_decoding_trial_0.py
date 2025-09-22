# Function to find an index based on user input
def find_index():
    # Step 1: Accept input from the user and convert it to a positive integer
    user_input = input()  # Get input from the user
    number = abs(int(user_input))  # Convert to integer and take absolute value

    # Step 2: Initialize a variable to track iterations
    index = 0

    # Step 3: Enter an infinite loop to find the solution
    while True:
        # Calculate the sum of the first `index` numbers
        sum_values = (index * (index + 1)) // 2
        
        # Calculate the difference between sum and the input number
        difference = sum_values - number

        # Step 4: Check if the sum is exactly equal to the number
        if sum_values == number:
            print(index)  # Output the current index
            break  # Exit the loop
        
        # Step 5: Check if the sum exceeds the input number
        elif sum_values > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Exit the loop

        # Step 6: Increment the index for the next iteration
        index += 1

# Example of calling the function
find_index()  # This will run the function to find the appropriate index based on input
