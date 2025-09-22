# Begin the program
def main():
    # Take an integer input from the user and store its absolute value
    absolute_value = abs(int(input()))

    # Initialize a counter variable for the iterative process
    counter = 0

    # Start an infinite loop to calculate triangular numbers
    while True:
        # Calculate the triangular number for the current counter position
        triangular_number = (counter * (counter + 1)) // 2
        
        # Calculate the difference between the triangular number and the input value
        difference = triangular_number - absolute_value
        
        # Check if the triangular number is exactly equal to the input value
        if triangular_number == absolute_value:
            # Print the current counter as the result
            print(counter)
            # Exit the loop as the result is found
            break

        # Check if the triangular number exceeds the input value
        elif triangular_number > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                # Print the current counter as the result
                print(counter)
                # Exit the loop as the result is found
                break

        # Increment the counter to check the next triangular number
        counter += 1

# Invoke the main function to run the program
if __name__ == "__main__":
    main()
