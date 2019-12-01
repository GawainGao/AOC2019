def solution():
    sum = 0
    sum2 = 0
    with open('Day01.txt') as f:
        for line in f.readlines():
            sum += int(line) // 3 - 2
            fuel = int(line)
            while fuel > 8:
                fuel = fuel // 3 - 2
                sum2 += fuel
    return sum, sum2

if __name__ == '__main__':
    print('First question:', solution()[0])
    print('Second question:', solution()[1])

