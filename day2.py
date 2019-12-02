def getNums():
    with open('day2.txt') as f:
        line = f.readlines()
        nums = line[0].split(',')
    intNums = [int(x) for x in nums]
    return intNums

def solution1(li):
    l = len(li)
    flag = 0
    while li[flag] != 99:
        if li[flag] == 1:
            li[li[flag+3]] = li[li[flag+2]]+li[li[flag+1]]
        elif li[flag] == 2:
            li[li[flag+3]] = li[li[flag+2]]*li[li[flag+1]]
        flag = flag + 4
        if flag > 109 or li[flag+1]>112 or li[flag+2]>112:
            return li
    return li

def changeNums(noun,verb,li):
    li[1] = noun
    li[2] = verb
    return(li)

if __name__ == '__main__':
    #Solution1
    print(solution1(getNums()))
    #Solution2
    for i in range(0, 100):
        for j in range(0, 100):
            li = getNums()
            if solution1(changeNums(i, j, li))[0] == 19690720:
                print(i*100+j)
                break
            
