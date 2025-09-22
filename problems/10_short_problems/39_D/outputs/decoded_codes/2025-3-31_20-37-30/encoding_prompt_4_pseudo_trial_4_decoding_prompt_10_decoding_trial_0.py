def main():
    # Read two lines of input
    input1 = input()
    input2 = input()
    
    # Split the input strings into lists
    elements1 = input1.split()
    elements2 = input2.split()
    
    # Initialize a result counter for discrepancies
    discrepancy_count = 0
    
    # Compare corresponding elements in the two lists
    for index in range(3):
        # Convert the current element to an integer
        a = int(elements1[index])
        b = int(elements2[index])
        
        # Check if the elements are different
        if a != b:
            discrepancy_count += 1
    
    # Determine if discrepancies are less than 3
    if discrepancy_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
