def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

def inside(x1, y1, x2, y2, x3, y3, x4, y4):
    return area(x1, y1, x2, y2, x3, y3) == (
        area(x4, y4, x2, y2, x3, y3) + 
        area(x1, y1, x4, y4, x3, y3) + 
        area(x1, y1, x2, y2, x4, y4)
    )

n = int(input())

for i in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
    
    if inside(x1, y1, x2, y2, x3, y3, x4, y4):
        print("INSIDE")
    else:
        print("OUTSIDE")
