# Function to find an index such that the sum of the first 'index' integers
# matches or meets certain conditions relative to user input
def find_index():
    # Step 1: Read user input and prepare the variable
    user_input = abs(int(input()))  # Get absolute integer value from user input

    # Step 2: Initialize the variable for loop control
    index = 0

    # Step 3: Use an indefinite loop to find the solution
    while True:
        # Step 4: Calculate the sum of the first 'index' integers
        sum_of_integers = (index * (index + 1)) // 2  # Using integer division
        
        # Step 5: Calculate the difference between the sum and user input
        difference = sum_of_integers - user_input
        
        # Step 6: Check if the sum matches the user input
        if sum_of_integers == user_input:
            print(index)  # Output the index if it's a match
            break  # Exit the loop
        
        # Step 7: Check if the sum exceeds the user input
        elif sum_of_integers > user_input:
            # Step 8: Check if the difference is even
            if difference % 2 == 0:  # Check if difference is even
                print(index)  # Output the index if the condition is met
                break  # Exit the loop
        
        # Step 9: Increment the index to try the next integer
        index += 1

# Call the function to execute
find_index()
