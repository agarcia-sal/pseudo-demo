def main():
    # Read a non-negative integer input from the user
    number = abs(int(input()))  # Ensure the input is non-negative

    # Initialize a counter variable
    counter = 0

    # Infinite loop to calculate and check certain conditions
    while True:
        # Calculate the sum of the first 'counter' natural numbers
        sum_of_naturals = (counter * (counter + 1)) // 2
        
        # Determine the difference between the calculated sum and the input number
        difference = sum_of_naturals - number

        # Check if the calculated sum equals the input number
        if sum_of_naturals == number:
            print(counter)  # Print the current counter value as the result
            break  # Exit the loop
        
        # Check if the calculated sum exceeds the input number
        elif sum_of_naturals > number:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(counter)  # Print the current counter value as the result
                break  # Exit the loop

        # Increment the counter for the next iteration
        counter += 1


if __name__ == "__main__":
    main()
