def part1(path):
    f = open(path, 'r')
    
    ans = 0
    comb = {
        'A X\n': 4,
        'A Y\n': 8,
        'A Z\n': 3,
        'B X\n': 1,
        'B Y\n': 5,
        'B Z\n': 9,
        'C X\n': 7,
        'C Y\n': 2,
        'C Z\n': 6
    }

    for x in f:
        ans += comb[x]

    print('Answer Part 1:', ans)

def part2(path):
    f = open(path, 'r')
    
    ans = 0
    comb = {
        'A X\n': 3,
        'A Y\n': 4,
        'A Z\n': 8,
        'B X\n': 1,
        'B Y\n': 5,
        'B Z\n': 9,
        'C X\n': 2,
        'C Y\n': 6,
        'C Z\n': 7
    }

    for x in f:
        ans += comb[x]

    print('Answer Part 2:', ans)


if __name__ == '__main__':
    #path to the input file
    path = './code/day2/input.txt'
    
    part1(path)
    part2(path)