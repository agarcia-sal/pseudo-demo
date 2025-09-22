def main():
    # Step 1: Accept user input for the size of the array
    size = int(input())

    # Step 2: Initialize a boolean array `status` of length `size` with all values set to True
    status = [True] * size

    # Step 3: Set initial variables
    index = 0
    increment = 1

    # Step 4: Loop until the increment is greater than 500,000
    while increment <= 500000:
        # Step 5: Check current status
        if status[index]:
            # Step 6: Update status and increment
            status[index] = False
            
        # Step 7: Increment and update index
        increment += 1
        index = (index + increment) % size

    # Step 8: Filter active status
    active_status = [s for s in status if s]

    # Step 9: Determine if any True elements exist
    if len(active_status) == 0:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
