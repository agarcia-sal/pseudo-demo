def find_integer():
    # Start the program and read input from the user
    userInput = abs(int(input()))  # Take the absolute value of the input integer
    
    # Initialize the index to represent the current integer being examined
    index = 0

    # Create an infinite loop to continue examining integers
    while True:
        # Calculate the sum of the first 'index' integers
        sum_of_integers = (index * (index + 1)) // 2  # Use integer division for precision

        # Calculate the difference value
        difference = sum_of_integers - userInput

        # Check if the sum equals userInput
        if sum_of_integers == userInput:
            print(index)  # Print index as the solution
            break  # End the program
        
        # Check if the sum is greater than userInput
        if sum_of_integers > userInput:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print index as the solution
                break  # End the program

        # Increment the index by 1 to check the next integer
        index += 1

# Call the function to execute the program
find_integer()
