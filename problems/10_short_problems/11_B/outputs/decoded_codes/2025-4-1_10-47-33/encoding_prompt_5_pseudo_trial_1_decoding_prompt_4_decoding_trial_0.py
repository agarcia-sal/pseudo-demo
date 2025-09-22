def main():
    # Read an integer input from the user (taking absolute value)
    user_input = abs(int(input()))
    
    # Initialize a variable index to represent the current integer we are examining
    index = 0

    # Create an infinite loop to continue examining integers
    while True:
        # Calculate the sum of the first 'index' integers using the formula
        sum_of_integers = (index * (index + 1)) // 2
        
        # Calculate the difference value
        difference = sum_of_integers - user_input

        # Check if the sum equals user_input
        if sum_of_integers == user_input:
            print(index)
            break  # End the program

        # Check if the sum is greater than user_input
        if sum_of_integers > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # End the program

        # Increment the index by 1 to check the next integer
        index += 1

# Call the main function to execute the program
main()
