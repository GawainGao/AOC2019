
#get values
def getValue(nums, mode, pos):
    if mode == 0:
        #print(nums[nums[pos]])
        return nums[nums[pos]]
    else:
        return nums[pos]

def getPos(nums, mode, pos):
    if mode == 0:
        return nums[pos]
    else:
        return pos
def doOne(nums, pos, inp, res, flag):
    #print(inp)
    instructions = nums[pos]
    op = instructions % 100
    if op != 99:
        #print(instructions)
        mode1 = instructions % 1000 // 100
        mode2 = instructions % 10000 // 1000
        mode3 = instructions % 100000 // 10000
        #print(mode1, mode2, mode3)
        if op == 1:
            #print('check:', pos+3, pos+1, pos+2)
            nums[getPos(nums, mode3, pos+3)] = getValue(nums, mode1, pos+1)+getValue(nums, mode2, pos+2)
            return nums, pos+4, res, flag
        elif op == 2:
            nums[getPos(nums, mode3, pos+3)] = getValue(nums, mode1, pos+1)*getValue(nums, mode2, pos+2)
            return nums, pos+4, res, flag
        elif op == 3:
            if flag:
                #print(inp[1])
                nums[nums[pos+1]] = inp[1]
                flag = False
            else:
                #print(inp[0])
                nums[nums[pos+1]] = inp[0]
            return nums, pos+2, res, flag
        elif op == 4:
            res.append(nums[nums[pos+1]])
            return nums, pos+2, res, flag
        elif op == 5:
            pos = getValue(nums, mode2, pos+2) if getValue(nums, mode1, pos+1) else pos+3
            return nums, pos, res, flag
        elif op == 6:
            pos = getValue(nums, mode2, pos+2) if getValue(nums, mode1, pos+1)==0 else pos+3
            return nums, pos, res, flag
        elif op == 7:
            nums[getPos(nums, mode3, pos+3)] = 1 if getValue(nums, mode1, pos+1) < getValue(nums, mode2, pos+2) else 0
            return nums, pos+4, res, flag
        elif op == 8:
            nums[getPos(nums, mode3, pos+3)] = 1 if getValue(nums, mode1, pos+1) == getValue(nums, mode2, pos+2) else 0
            return nums, pos+4, res, flag
    else:
        return nums, -1, res, flag

def amplify(nums, phaseList, thrusters):
    res = []
    numsCopy = nums[:]
    for i in range(5):
        isFirstTime = True
        output = res[0] if len(res) else thrusters
        pos = 0
        res = []
        nums = numsCopy[:]
        inp = [output, phaseList[i]]
        #print(inp)
        while pos!= -1:
        #for i in range(5):
            nums, pos, res, isFirstTime = doOne(nums, pos, inp, res, isFirstTime)
            #print(nums)
            #print('pos:',pos, ' res:',res)
            #print(nums)
    #print(res)
    return res[0]

if __name__=="__main__":
    #with open('day7.txt') as f:
    #with open('test.txt') as f:
    with open('test2.txt') as f:
        line = f.read().split(',')
        nums = [int(x) for x in line]
    #print(nums)
    phaseList1 = [4,3,2,1,0]
    phaseList2 = [5,6,7,8,9]
    phaseList = phaseList2
    res = 0
    newres = 0
    thr = 0
    maxres = 0
    for a in phaseList:
        for b in phaseList:
            if a != b:
                for c in phaseList:
                    if a!=c and b !=c:
                        for d in phaseList:
                            if d!=a and d!=b and d!=c:
                                for e in phaseList:
                                    if e!=a and e!=b and e!=c and e!=d:
                                        li = [a,b,c,d,e]
                                        #res = max(res, amplify(nums, li, 0))
                                        for i in range(10):
                                            #if a == 9 and b == 8 and c == 7 and d == 6:
                                            if a == 9 and b == 7 and c == 8 and d == 5:
                                                res = amplify(nums, li, res)
                                                print(res, nums)
                                        #     res = newres
                                        #     newres = amplify(nums, li, res)
                                        #     print(newres)
                                        # maxres = max((maxres), newres)
    print(res)