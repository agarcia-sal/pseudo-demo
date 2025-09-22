def do_main():
    # Read two lines of input
    input1 = input()
    input2 = input()
    
    # Split the two input strings by space into lists
    list1 = input1.split()
    list2 = input2.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        num1 = int(list1[index])
        num2 = int(list2[index])
        
        # Check if the integers are different
        if num1 != num2:
            # Increment the difference counter
            difference_count += 1
    
    # Check the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    do_main()
