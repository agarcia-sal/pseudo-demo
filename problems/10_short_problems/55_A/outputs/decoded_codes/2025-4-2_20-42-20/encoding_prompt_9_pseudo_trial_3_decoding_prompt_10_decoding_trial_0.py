def main():
    # Accept input for the size of the array
    size = int(input())
    
    # Initialize an array of booleans, All set to True
    status = [True] * size

    # Set initial variables
    index = 0
    increment = 1

    # Loop until the increment exceeds 500,000
    while increment <= 500000:
        # Check current status
        if status[index]:
            status[index] = False
        
        # Update values
        increment += 1
        index = (index + increment) % size

    # Filter active status
    active_status = [s for s in status if s]

    # Determine if any True elements exist
    if len(active_status) == 0:
        print("YES")
    else:
        print("NO")

# Start the program
if __name__ == "__main__":
    main()
