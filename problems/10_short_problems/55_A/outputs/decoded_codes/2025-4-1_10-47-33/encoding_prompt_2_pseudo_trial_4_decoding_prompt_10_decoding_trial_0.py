def main():
    # Input: Read the integer value for the size of the array
    n = int(input())
    
    # Initialize the list to track availability of each position
    is_available = [True] * n
    current_position = 0  # Starting index
    increment = 1         # Step size

    # Processing Loop: Continue until increment exceeds 500,000
    while increment <= 500000:
        if is_available[current_position]:
            is_available[current_position] = False
        
        increment += 1  # Increase the increment for next step
        current_position = (current_position + increment) % n  # Move to the next position

    # Identify unavailable positions
    available_positions = [pos for pos in is_available if pos]
    
    # Output: Check if there are any available positions
    if len(available_positions) == 0:
        print("YES")  # All positions are unavailable
    else:
        print("NO")   # There are some available positions

# Run the main function
if __name__ == "__main__":
    main()
