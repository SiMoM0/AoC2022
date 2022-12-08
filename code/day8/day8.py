grid = []

def read_input(path):
    with open(path, 'r') as f:
        for line in f:
            #create grid
            grid.append([int(x) for x in line if x != '\n'])

def part1():    
    visible = set()

    #from left
    for i in range(1, len(grid)-1):
        tall = grid[i][0]
        for j in range(1, len(grid)-1):
            if grid[i][j] > tall:
                visible.add((i, j))
                tall = grid[i][j]
    
    #from right
    for i in range(1, len(grid)-1):
        tall = grid[i][len(grid)-1]
        for j in range(len(grid)-2, 0, -1):
            if grid[i][j] > tall:
                visible.add((i, j))
                tall = grid[i][j]

    #from top
    for i in range(1, len(grid)-1):
        tall = grid[0][i]
        for j in range(1, len(grid)-1):
            if grid[j][i] > tall:
                visible.add((j, i))
                tall = grid[j][i]

    #from bottom
    for i in range(1, len(grid)-1):
        tall = grid[len(grid)-1][i]
        for j in range(len(grid)-2, 0, -1):
            if grid[j][i] > tall:
                visible.add((j, i))
                tall = grid[j][i]

    ans = len(grid) * 4 - 4 + len(visible)
    print('Answer Part 1: ', ans)

def part2():
    ans = 0

    for i in range(1, len(grid)-1):
        for j in range(1, len(grid)-1):
            height = grid[i][j]
            trees = [0, 0, 0, 0]

            #look right
            for k in range(j+1, len(grid)):
                trees[0] += 1
                if height <= grid[i][k]:
                    break

            #look left
            for k in range(j-1, -1, -1):
                trees[1] += 1
                if height <= grid[i][k]:
                    break

            #look up
            for k in range(i-1, -1, -1):
                trees[2] += 1
                if height <= grid[k][j]:
                    break

            #look down
            for k in range(i+1, len(grid)):
                trees[3] += 1
                if height <= grid[k][j]:
                    break

            ans = max(ans, trees[0]*trees[1]*trees[2]*trees[3])

    print('Answer Part 2: ', ans)

if __name__ == '__main__':
    #path to input file
    path = './code/day8/input.txt'
    read_input(path)

    part1()
    part2()