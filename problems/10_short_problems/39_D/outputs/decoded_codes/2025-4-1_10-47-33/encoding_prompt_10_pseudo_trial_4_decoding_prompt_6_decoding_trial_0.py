def do_main():
    # Input two strings
    input_string1 = input()
    input_string2 = input()
    
    # Split input strings into lists of strings
    list1 = input_string1.split()
    list2 = input_string2.split()
    
    # Initialize a result counter
    difference_count = 0
    
    # Loop through the first three elements of the lists
    for index in range(3):
        # Convert string elements of both lists to integers
        value1 = int(list1[index])
        value2 = int(list2[index])
        
        # Check if the values from both lists are not equal
        if value1 != value2:
            # Increment the result counter
            difference_count += 1
            
    # Check the total number of different elements
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    do_main()
