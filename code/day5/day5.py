def part1(path):
    stacks = []
    #flag to control boxes (True) or moving part (False)
    flag = True
    with open(path, 'r') as f:
        line = f.readline()
        stacks = [[] for i in range(len(line)//4)]
        for i in range(0, len(line)-3, 4):
            if line[i:i+3] != '   ':
                stacks[i//4].append(line[i+1])
        for line in f:
            if line[1] == '1':
                #jump to moving part and change flag
                next(f)
                flag = False
            elif flag:
                for i in range(0, len(line)-3, 4):
                    if line[i:i+3] != '   ':
                        stacks[i//4].append(line[i+1])
            else:
                moves = line.split(' ')
                for i in range(int(moves[1])):
                    elem = stacks[int(moves[3])-1].pop(0)
                    stacks[int(moves[5])-1].insert(0, elem)

    print('Answer Part 1: ', [s[0] for s in stacks])

def part2(path):
    stacks = []
    #flag to control boxes (True) or moving part (False)
    flag = True
    with open(path, 'r') as f:
        line = f.readline()
        stacks = [[] for i in range(len(line)//4)]
        for i in range(0, len(line)-3, 4):
            if line[i:i+3] != '   ':
                stacks[i//4].append(line[i+1])
        for line in f:
            if line[1] == '1':
                #jump to moving part and change flag
                next(f)
                flag = False
            elif flag:
                for i in range(0, len(line)-3, 4):
                    if line[i:i+3] != '   ':
                        stacks[i//4].append(line[i+1])
            else:
                moves = line.split(' ')
                stacks[int(moves[5])-1][:0] = stacks[int(moves[3])-1][0:int(moves[1])]
                stacks[int(moves[3])-1] = stacks[int(moves[3])-1][int(moves[1]):]

    print('Answer Part 2: ', [s[0] for s in stacks])

if __name__ == '__main__':
    #path to input file
    path = './code/day5/input.txt'

    part1(path)
    part2(path)