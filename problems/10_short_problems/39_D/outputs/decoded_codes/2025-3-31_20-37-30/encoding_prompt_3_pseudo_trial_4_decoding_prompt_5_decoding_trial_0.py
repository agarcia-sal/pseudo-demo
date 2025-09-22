def main():
    # Take input for comparison
    string1 = input()
    string2 = input()

    # Split the input strings into lists of strings
    list1 = string1.split()
    list2 = string2.split()
    
    # Initialize a counter for differences
    difference_counter = 0 

    # Compare corresponding elements in the lists
    for index in range(3):  # Assuming both lists have at least 3 elements
        # Convert the current elements to integers for comparison
        value1 = int(list1[index])
        value2 = int(list2[index])
        
        # Check if the values are different
        if value1 != value2:
            difference_counter += 1  # Incrementing the counter if values differ
            
    # Determine if the number of differences is less than 3
    if difference_counter < 3:
        print("YES")  # There are fewer than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# Entry point of the program
if __name__ == "__main__":
    main()
