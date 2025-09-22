def main():
    # Start the program by reading user input
    total_count = int(input())  # Read total count of entries

    # Initialize the list with True values
    is_marked = [True] * total_count

    # Set initial counters for the processing loop
    current_step = 1
    index = 0

    # Processing loop to mark entries as False
    while current_step <= 500000:
        if is_marked[index]:  # Check if the current index is marked True
            is_marked[index] = False  # Mark the position as processed
        current_step += 1  # Increment the step
        index = (index + current_step) % total_count  # Update the index with wrap-around

    # Create a list of entries that are still True (unmarked)
    remaining_true = [marked for marked in is_marked if marked]

    # Determine and print the final output
    if not remaining_true:  # If no entries are True, output "YES"
        print("YES")
    else:  # If there are still True entries, output "NO"
        print("NO")

# Run the main function to execute the program
if __name__ == "__main__":
    main()
