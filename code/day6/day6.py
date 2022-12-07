def part1(path):
    index = 4
    with open(path, 'r') as f:
        sequence = f.read(4)

        while len(set(sequence)) != 4:
            sequence = sequence[1:] + f.read(1)
            index += 1

    print('Answer Part 1: ', index)

def part2(path):
    index = 14
    with open(path, 'r') as f:
        sequence = f.read(14)

        while len(set(sequence)) != 14:
            sequence = sequence[1:] + f.read(1)
            index += 1

    print('Answer Part 2: ', index)

if __name__ == '__main__':
    #path to input file
    path = './code/day6/input.txt'

    part1(path)
    part2(path)