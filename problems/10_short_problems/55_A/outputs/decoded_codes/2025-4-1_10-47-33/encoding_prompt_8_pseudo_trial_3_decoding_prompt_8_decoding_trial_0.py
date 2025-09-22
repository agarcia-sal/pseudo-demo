def main():
    # Get Input
    n = int(input())
    
    # Initialize List
    marked = [True] * n  # All positions are initially unmarked
    
    # Set Initial Variables
    currentIndex = 0
    step = 1
    
    # Mark Unmarked Positions
    while step <= 500000:
        if marked[currentIndex]:  # If the position is unmarked
            marked[currentIndex] = False  # Mark it
        step += 1  # Increase step for the next iteration
        currentIndex = (currentIndex + step) % n  # Move to the next position circularly
    
    # Check for Unmarked Positions
    unmarkedPositions = [pos for pos in marked if pos]  # List of unmarked positions
    
    # Determine Output
    if not unmarkedPositions:  # If the list is empty
        print("YES")  # All positions were marked
    else:
        print("NO")  # There are still unmarked positions

# Call the main function
main()
