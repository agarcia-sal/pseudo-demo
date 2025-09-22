def main():
    # Get the absolute value of a number input from the user
    user_input = input()
    n = abs(int(user_input))  # Ensure input is an integer and get its absolute value
    i = 0  # Initialize index variable

    while True:
        # Calculate the sum of the first i integers
        sum_of_first_i = (i * (i + 1)) // 2  # Use integer division for precise results
        
        # Calculate the difference between the sum and n
        difference = sum_of_first_i - n
        
        # Check if the sum equals n
        if sum_of_first_i == n:
            print(i)  # Print the value of i
            break  # Exit the loop

        # Check if the sum is greater than n
        elif sum_of_first_i > n:
            # Check if the difference is even
            if difference % 2 == 0:  # Use modulo operator to check for even
                print(i)  # Print the value of i
                break  # Exit the loop
        
        # Increment i for the next iteration
        i += 1

# Run the main function
if __name__ == '__main__':
    main()
