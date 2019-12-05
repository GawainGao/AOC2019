
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
def doOne(nums, pos):
    inp = 5
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
            return nums, pos+4
        elif op == 2:
            nums[getPos(nums, mode3, pos+3)] = getValue(nums, mode1, pos+1)*getValue(nums, mode2, pos+2)
            return nums, pos+4
        elif op == 3:
            nums[nums[pos+1]] = inp
            return nums, pos+2
        elif op == 4:
            print(nums[nums[pos+1]])
            return nums, pos+2
        elif op == 5:
            return nums, getValue(nums, mode2, pos+2) if getValue(nums, mode1, pos+1) else pos+3
        elif op == 6:
            return nums, getValue(nums, mode2, pos+2) if getValue(nums, mode1, pos+1)==0 else pos+3
        elif op == 7:
            nums[getPos(nums, mode3, pos+3)] = 1 if getValue(nums, mode1, pos+1) < getValue(nums, mode2, pos+2) else 0
            return nums, pos+4
        elif op == 8:
            nums[getPos(nums, mode3, pos+3)] = 1 if getValue(nums, mode1, pos+1) == getValue(nums, mode2, pos+2) else 0
            return nums, pos+4
    else:
        return nums, -1
if __name__=="__main__":
    with open('day5.txt') as f:
        line = f.read().split(',')
        nums = [int(x) for x in line]
    #print(nums)
    pos = 0
    while pos!= -1:
    #for i in range(5):
        nums, pos = doOne(nums, pos)
        print('pos:',pos)
        #print(nums)
