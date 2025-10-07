def fruit_distribution(s: str, n: int) -> int:
    lis = []
    for i in s.split(" "):
        if i.isdigit() == True:
            lis.append(int(i))
    total_apples_and_oranges = 0
    for number in lis:
        total_apples_and_oranges = total_apples_and_oranges + number
    mango_fruits = n - total_apples_and_oranges
    return mango_fruits