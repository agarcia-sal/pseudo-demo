# Codeforces Round 20
# Problem A: BerOS File System

def normalize(path):
    normal = ""
    for i in range(len(path)):
        if (path[i] != ""):
            normal += "/" + path[i]
    if (normal == ""):
        return "/"
    return normal

path = input("").split("/")
print(normalize(path))
