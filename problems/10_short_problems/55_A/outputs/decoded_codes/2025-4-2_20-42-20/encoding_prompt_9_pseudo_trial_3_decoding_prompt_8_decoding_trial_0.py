def main():
    # Accept Input
    size = int(input())

    # Initialize Array
    status = [True] * size

    # Set Initial Variables
    index = 0
    increment = 1

    # Loop until a condition is met
    while increment <= 500000:
        # Check Current Status
        if status[index]:
            status[index] = False
        
        # Update Values
        increment += 1
        index = (index + increment) % size

    # Filter Active Status
    active_status = [s for s in status if s]

    # Determine If Any True Elements Exist
    if len(active_status) == 0:
        print("YES")
    else:
        print("NO")

# End Program
if __name__ == "__main__":
    main()
