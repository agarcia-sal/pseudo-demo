def main():
    # Initialize Input
    n = int(input())  # Read an integer for the size of the list.

    # Create a Boolean List
    isActive = [True] * n  # Initialize the list with True values.

    # Set Up Variables
    index = 0
    counter = 1

    # Iterate While Counter is Less Than or Equal To 500000
    while counter <= 500000:
        if isActive[index]:  # Check if the current index is active
            isActive[index] = False  # Deactivate the current index
        counter += 1  # Increment the counter
        index = (index + counter) % n  # Update the index using modulo to wrap around

    # Filter Active Elements
    activeElements = [active for active in isActive if active]  # List of True values

    # Check Active Elements
    if len(activeElements) == 0:
        print("YES")  # Output "YES" if no elements are active
    else:
        print("NO")  # Output "NO" if there are still active elements

# Call the main function if this script is run
if __name__ == "__main__":
    main()
