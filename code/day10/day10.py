def part1(path):
    ans = []

    #register
    x = 1

    with open(path, 'r') as f:
        #flag True if the next instruction can be read
        flag = True
        #number to add
        num = 0
        for i in range(1, 221):
            if (i-20) % 40 == 0:
                ans.append(x*i)

            if flag:
                line = f.readline()
                operation = line.split(' ')
                
                if operation[0] == 'noop\n':
                    continue

                flag = False
                num = operation[1]
            else:
                x += int(num)
                flag = True

    print('Answer Part 1: ', sum(ans))

def part2(path):
    ans = []

    #register
    x = 1
    #sprite position
    sprite = 0

    with open(path, 'r') as f:
        #flag True if the next instruction can be read
        flag = True
        #number to add
        num = 0
        #line of pixels
        pixels = ''
        for i in range(1, 240):
            if sprite <= (i-1)%40 <= sprite + 2:
                pixels += '#'
            else:
                pixels += ' '

            if flag:
                line = f.readline()
                operation = line.split(' ')
                
                if operation[0] == 'noop\n':
                    continue

                flag = False
                num = operation[1]
            else:
                x += int(num)
                flag = True
                
                #update sprite start
                sprite += int(num)

    print('Answer Part 2: ')
    for i in range(0, 240, 40):
        print(pixels[i:i+40])

if __name__ == '__main__':
    #path to input file
    path = './code/day10/input.txt'

    part1(path)
    part2(path)