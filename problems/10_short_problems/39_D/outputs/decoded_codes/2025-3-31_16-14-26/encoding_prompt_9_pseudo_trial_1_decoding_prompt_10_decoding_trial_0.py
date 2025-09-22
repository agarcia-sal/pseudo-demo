def main():
    # Receive Input
    first_input = input()  # First set of integers as a string
    second_input = input()  # Second set of integers as a string

    # Split Input into Individual Numbers
    first_set = list(map(int, first_input.split()))
    second_set = list(map(int, second_input.split()))
    
    # Initialize Difference Counter
    difference_count = 0

    # Compare Corresponding Items
    for index in range(3):
        first_number = first_set[index]
        second_number = second_set[index]
        
        if first_number != second_number:
            difference_count += 1

    # Determine Result Based on Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execution Trigger
if __name__ == "__main__":
    main()
