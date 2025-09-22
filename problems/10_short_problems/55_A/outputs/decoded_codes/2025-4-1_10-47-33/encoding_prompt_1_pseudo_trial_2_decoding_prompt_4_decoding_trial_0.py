def main():
    # Step 1: Initialize Input
    n = int(input())  # Read the size of the list

    # Step 2: Create a Boolean List
    isActive = [True] * n  # Initialize a list of True with size n

    # Step 3: Set Up Variables
    index = 0
    counter = 1

    # Step 4: Iterate While Counter is Less Than or Equal To 500000
    while counter <= 500000:
        if isActive[index]:  # If the current position is True
            isActive[index] = False  # Set it to False

        counter += 1  # Increment the counter
        index = (index + counter) % n  # Update index with wrap-around using modulo

    # Step 5: Filter Active Elements
    activeElements = [active for active in isActive if active]  # Get only True values

    # Step 6: Check Active Elements
    if len(activeElements) == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
