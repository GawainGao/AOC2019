import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def moveTo(self, d):
        directrion = {'U':[0,1],'D':[0,-1],'L':[-1,0],'R':[1,0]}
        return Point(self.x + directrion[d][0],self.y+directrion[d][1])

def wireList(li):
    xaixs = []
    yaixs = []
    res = {}
    flag = 0
    point = Point(50000,50000)
    xaixs.append(point.x)
    yaixs.append(point.y)
    for i in range(len(li)):
        for j in range(int(li[i][1:])):
            flag += 1
            point = point.moveTo(li[i][0])
            xaixs.append(point.x)
            yaixs.append(point.y)
            if (point.x,point.y) not in res:
                res[(point.x,point.y)] = flag
    return(res, xaixs, yaixs)
if __name__ == '__main__':
    with open('day3.txt') as f:
        A, B = [x.split(',') for x in f.readlines()]

    a,ax,ay = wireList(A)
    b,bx,by = wireList(B)
    plt.plot(ax,ay)
    plt.plot(bx,by)
    plt.show()
    cross = a.keys() & b.keys()
    print(cross)

    #Solution1
    print(min(abs(x-50000)+abs(y-50000) for x,y in cross))
    #Solution2
    print(min(a[p]+b[p] for p in cross))