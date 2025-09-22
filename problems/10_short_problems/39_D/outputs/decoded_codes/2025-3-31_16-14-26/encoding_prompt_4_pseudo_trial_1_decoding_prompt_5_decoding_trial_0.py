def main():
    # Read input values
    input1 = input()
    input2 = input()
    
    # Split input strings into lists of strings
    list1 = input1.split()
    list2 = input2.split()
    
    # Initialize a count of differences
    difference_count = 0 
    
    # Compare corresponding elements of the two lists
    for i in range(3):
        # Convert elements to integers
        value1 = int(list1[i])
        value2 = int(list2[i])
        
        # Count the differences
        if value1 != value2:
            difference_count += 1 
    
    # Determine if the differences are fewer than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
