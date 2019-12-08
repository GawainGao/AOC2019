
from matplotlib import pyplot as plt
def count0(p):
    res = 0
    for i in p:
        if i == '0':
            res += 1
    return res

def count1(p):
    res = 0
    for i in p:
        if i == '1':
            res += 1
    return res

def count2(p):
    res = 0
    for i in p:
        if i == '2':
            res += 1
    return res



if __name__=='__main__':
    with open('day8.txt') as f:
        pixels = str(f.read())
        print(pixels)
    i = 0
    sa0 = 150
    ma1 = 0
    ma2 = 0
    while i < len(pixels):
        if sa0 > count0(pixels[i:i+150]):
            sa0 = count0(pixels[i:i+150])
            ma1 = count1(pixels[i:i+150])
            ma2 = count2(pixels[i:i+150])
        i = i + 150
        print(sa0, ma1, ma2)
    print(ma1, ' ', ma2)
    print(ma1 * ma2)

    print(len(pixels) // 150)
    #100 layers
    res = []
    for a in range(150):
        temp = a
        while pixels[temp] == '2':
            temp += 150
        res.append(pixels[temp])
    print(res)
    map = [[0 for i in range(25)] for j in range(6)]
    for a in range(6):
        for b in range(25):
            if res[a*25+b] == '0':
                map[a][b] = 255
            else:
                map[a][b] = 0
    plt.imshow(map)
    plt.show()
    print(map)