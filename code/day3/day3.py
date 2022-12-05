#items and their priority
items = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
            'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}


def part1(path):
    f = open(path, 'r')

    ans = 0

    for x in f:
        half = len(x) // 2
        letter = list(set(x[:half]) & set(x[half:]))[0]
        ans += items[letter]

    print('Answer Part 1:', ans)

def part2(path):
    ans = 0

    with open(path, 'r') as f:
        for line in f:
            set1 = set(line.strip())
            set2 = set(next(f).strip())
            set3 = set(next(f).strip())

            ans += items[list(set1 & set2 & set3)[0]]

    print('Answer Part 2:', ans)

if __name__ == '__main__':
    #path to the input file
    path = './code/day3/input.txt'

    part1(path)
    part2(path)