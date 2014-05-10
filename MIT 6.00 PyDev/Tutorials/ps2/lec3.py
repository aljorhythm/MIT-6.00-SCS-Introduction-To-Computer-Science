def isPerfectCube(x):
    i = 0
    while i * i * i < abs(x):
        i += 1
    if i * i * i == abs(x):
        return True
    else:
        return False

def cubeRoot(x):
    i = 0
    while i * i * i < abs(x):
        i += 1
    if i * i * i == abs(x):
        return -i if x < 0 else i
    else:
        return False

print (isPerfectCube(999 * -999 * 999))
print (cubeRoot(-999*999*999))
