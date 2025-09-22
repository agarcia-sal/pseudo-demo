def main():
    # Step 1: Read Input
    n = int(input())
    
    # Step 2: Initialize the Marking List
    markings = [True] * n
    
    # Step 3: Set Initial Variables
    index = 0
    step = 1

    # Step 4: Start the Marking Process
    while step <= 500000:
        if markings[index]:  # If the current item is True
            markings[index] = False  # Mark it as False (processed)

        step += 1
        index = (index + step) % n  # Wrap around using modulo

    # Step 5: Check Remaining Marked Items
    remaining_true = [m for m in markings if m]  # Items still marked True

    # Step 6: Output Result
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the code
if __name__ == "__main__":
    main()
