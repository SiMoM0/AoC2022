def part1(path):
    ans = 0

    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            sections = line.split(',')
            interval1 = list(map(int, sections[0].split('-')))
            interval2 = list(map(int, sections[1].split('-')))
            
            #check if one fully contains the other
            if (interval1[0] <= interval2[0] and interval1[1] >= interval2[1]) or (interval2[0] <= interval1[0] and interval2[1] >= interval1[1]):
                ans += 1

    print('Answer Part 1: ', ans)

def part2(path):
    ans = 0

    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            sections = line.split(',')
            interval1 = list(map(int, sections[0].split('-')))
            interval2 = list(map(int, sections[1].split('-')))
            
            #check overlapping
            if interval1[0] <= interval2[1] and interval2[0] <= interval1[1]:
                ans += 1

    print('Answer Part 2: ', ans)

if __name__ == '__main__':
    #path to input file
    path = './code/day4/input.txt'

    part1(path)
    part2(path)