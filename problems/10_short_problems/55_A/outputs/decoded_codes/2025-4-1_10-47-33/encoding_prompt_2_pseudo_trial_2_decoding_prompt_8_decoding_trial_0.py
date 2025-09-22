def check_values_in_list():
    n = int(input())
    isActive = [True] * n
    currentIndex = 0
    increment = 1
    
    while increment <= 500000:
        if isActive[currentIndex]:
            isActive[currentIndex] = False
        
        increment += 1
        currentIndex = (currentIndex + increment) % n
    
    activeElements = [value for value in isActive if value]
    
    if len(activeElements) == 0:
        print("YES")
    else:
        print("NO")

check_values_in_list()
