def part1(file):
    values = {}
    path = []

    with open(file, 'r') as f:
        for line in f:
            val = line.split()
            if val[0] == '$':
                if val[1] == 'ls':
                    continue
                elif val[1] == 'cd' and val[2] == '/':
                    path.append('/')
                    values[''.join(path)] = 0
                elif val[1] == 'cd' and val[2] != '..':
                    path.append(val[2])
                    values[''.join(path)] = 0
                else:
                    path.pop()
            elif val[0] != 'dir':
                tempPath = ''
                for x in path:
                    tempPath += x
                    values[tempPath] += int(val[0])

    print('Answer Part 1:', sum([x for x in values.values() if x < 100000]))

def part2(file):
    values = {}
    path = []

    with open(file, 'r') as f:
        for line in f:
            val = line.split()
            if val[0] == '$':
                if val[1] == 'ls':
                    continue
                elif val[1] == 'cd' and val[2] == '/':
                    path.append('/')
                    values[''.join(path)] = 0
                elif val[1] == 'cd' and val[2] != '..':
                    path.append(val[2])
                    values[''.join(path)] = 0
                else:
                    path.pop()
            elif val[0] != 'dir':
                tempPath = ''
                for x in path:
                    tempPath += x
                    values[tempPath] += int(val[0])

    required = 30000000 - (70000000 - values['/'])

    print('Answer Part 2:', min([x for x in values.values() if x > required]))

if __name__ == '__main__':
    #path to input file
    file = './code/day7/input.txt'

    part1(file)
    part2(file)