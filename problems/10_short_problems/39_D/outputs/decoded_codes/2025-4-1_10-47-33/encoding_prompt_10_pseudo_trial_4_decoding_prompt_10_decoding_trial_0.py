def do_main():
    # Input two strings containing space-separated integers
    t1 = input()
    t2 = input()
    
    # Split input strings into lists of integers
    tt1 = list(map(int, t1.split()))
    tt2 = list(map(int, t2.split()))
    
    # Initialize a result counter
    res = 0
    
    # Loop through the first three elements of the lists
    for x in range(3):
        a = tt1[x]
        b = tt2[x]
        
        # Increment the result counter if the values from both lists are not equal
        if a != b:
            res += 1
            
    # Check the total number of different elements
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    do_main()
