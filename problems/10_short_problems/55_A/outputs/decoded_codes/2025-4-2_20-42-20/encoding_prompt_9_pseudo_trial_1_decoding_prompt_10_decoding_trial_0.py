def main():
    # Step 1: Read Input
    n = int(input())  # Get the total number of elements

    # Step 2: Initialize the Marking List
    markings = [True] * n  # Create a list of n elements, initialized to True

    # Step 3: Set Initial Variables
    index = 0  # Track current position in the markings list
    step = 1   # Indicates the current counting step

    # Step 4: Start the Marking Process
    while step <= 500000:
        # Mark the current item as False if it's still True
        if markings[index]:
            markings[index] = False

        # Increment step and calculate new index
        step += 1
        index = (index + step) % n  # Wrap around using modulo n

    # Step 5: Check Remaining Marked Items
    remaining_true = [mark for mark in markings if mark]  # Collect remaining True items

    # Step 6: Output Result
    if len(remaining_true) == 0:  # Check if there are no remaining True items
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
