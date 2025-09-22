def main():
    # Read input for first and second lists
    first_list = input()
    second_list = input()
    
    # Process the inputs by splitting the strings into lists of values
    first_values = first_list.split()
    second_values = second_list.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through each element in the range of 0 to 2 (inclusive)
    for x in range(3):
        value_a = int(first_values[x])
        value_b = int(second_values[x])
        
        # Increment the difference count if values are not equal
        if value_a != value_b:
            difference_count += 1
            
    # Output "YES" if differences are less than 3, otherwise "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function when the script is executed
if __name__ == "__main__":
    main()
