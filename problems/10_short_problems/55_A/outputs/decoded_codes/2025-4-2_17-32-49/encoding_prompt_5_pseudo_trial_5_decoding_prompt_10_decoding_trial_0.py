def main():
    # Input Section
    n = int(input())  # Prompt the user to enter a number n

    # Initialization
    boolean_list = [True] * n  # Create a list with n elements, all initially set to True
    current_index = 0
    counter = 1

    # Loop for Operations
    while counter <= 500000:
        if boolean_list[current_index]:  # Check if the current element is True
            boolean_list[current_index] = False  # Set the element to False
        
        counter += 1  # Increment counter
        current_index = (current_index + counter) % n  # Update currentIndex with wrap-around using modulo

    # Check Remaining True Values
    remaining_true = [value for value in boolean_list if value]  # List of True elements in boolean_list

    if len(remaining_true) == 0:  # Check if there are no True values left
        print("YES")  # Print YES if all elements are False
    else:
        print("NO")  # Print NO if any element is still True

if __name__ == "__main__":
    main()  # Run the main function
