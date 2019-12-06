if __name__ == '__main__':
    with open('day06.txt') as f:
    #with open('test.txt') as f:
        lines = f.readlines()
        inp = [line.strip() for line in lines]
        #print(inp)
    tree = {}
    for i in range(len(inp)):
        tree[inp[i][4:]] = inp[i][:3]
    #print(tree)
    s = 0
    for i in tree:
        m = 1
        #print(i)
        temp = i
        while tree[temp] in tree:
            m += 1
            temp = tree[temp]
        s += m
        #print(s)     
    #Solution1
    print('solution1:',s)
    route = []
    for i in tree:
        m = 1
        if i == 'YOU':
            temp = i
            while tree[temp] in tree:
                route.append(temp)
                m += 1
                temp = tree[temp]
            #print(m)
            #print(route)
    for i in tree:
        m = 1
        if i == 'SAN':
            temp = i
            while tree[temp] in tree and tree[temp] not in route:
                m += 1
                temp = tree[temp]
            a = route.index(tree[temp])
            res = a + m - 2
            print('solution2:',res)