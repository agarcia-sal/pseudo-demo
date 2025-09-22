def main():
    number_of_elements = int(input())
    flags = [True] * number_of_elements
    
    index = 0
    counter = 1
    
    while counter <= 500000:
        if flags[index]:
            flags[index] = False
        counter += 1
        index = (index + counter) % number_of_elements
    
    active_flags = [flag for flag in flags if flag]
    
    if not active_flags:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
