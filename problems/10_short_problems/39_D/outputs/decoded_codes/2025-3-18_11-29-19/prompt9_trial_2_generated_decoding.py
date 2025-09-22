def main():
    # Read the first line of input as the first list of numbers
    first_list = input().split()
    
    # Read the second line of input as the second list of numbers
    second_list = input().split()
    
    # Initialize difference counter
    difference_counter = 0

    # Compare elements at each position from 0 to 2
    for i in range(3):
        first_number = int(first_list[i])  # Convert the current element of the first list
        second_number = int(second_list[i])  # Convert the current element of the second list
        
        # Check if the numbers at the current position are not equal
        if first_number != second_number:
            difference_counter += 1  # Increment difference counter

    # Determine result based on the difference counter
    if difference_counter < 3:
        print("YES")  # Output "YES" if differences are fewer than 3
    else:
        print("NO")   # Output "NO" otherwise

# Call the main function
main()
