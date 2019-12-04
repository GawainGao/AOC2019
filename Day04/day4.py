def isTwo(li):
    for i in range(5):
        if int(li[i]) == int(li[i+1]):
            return True
    return False

def isThree(li):
    for i in range(4):
        if int(li[i]) == int(li[i+1]):
            if int(li[i+1]) == int(li[i+2]):
                return True
    return False

def isIncrease(li):
    for i in range(5):
        if int(li[i]) > int(li[i+1]):
                return False
    return True

def isOnlyTwo(li):
    res = {}
    for i in range(6):
        if li[i] in res:
            res[li[i]] += 1
        else:
            res[li[i]] = 1
    for i in res.keys():
        if res[i] == 2:
            return True
    return False


#307237-769058
if __name__=="__main__":
    print('test')
    solution1 = 0
    solution2 = 0
    for i in range(307237, 769059):
        if isTwo(str(i)) and isIncrease(str(i)):
            solution1 += 1
    print(solution1)
    for i in range(307237, 769059):
        if isOnlyTwo(str(i)) and isIncrease(str(i)):
            solution2 += 1
    print(solution2)