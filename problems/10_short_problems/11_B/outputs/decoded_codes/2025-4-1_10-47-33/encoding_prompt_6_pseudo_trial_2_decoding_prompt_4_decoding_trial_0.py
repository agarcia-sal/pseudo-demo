def main():
    # Get the absolute value of a number input from the user
    user_input = input()
    n = abs(int(user_input))  # Convert user input to an integer and take its absolute value
    i = 0  # Initialize an index variable

    while True:
        # Calculate the sum of the first i integers
        sum_of_first_i = (i * (i + 1)) // 2  # Using integer division
        
        # Calculate the difference between the sum and n
        difference = sum_of_first_i - n
        
        # Check if the sum equals n
        if sum_of_first_i == n:
            print(i)  # Print the value of i
            break  # Exit the loop

        # Check if the sum is greater than n
        elif sum_of_first_i > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(i)  # Print the value of i
                break  # Exit the loop

        # Increment i for the next iteration
        i += 1

# Call the main function to execute the program
if __name__ == "__main__":
    main()
