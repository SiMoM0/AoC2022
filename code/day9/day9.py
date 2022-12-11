def update_position(elem, move):
    '''
    Update position of head or tail by the input move (U, D, L, R).
    '''
    if move == 'U':
        elem[1] += 1
    elif move == 'D':
        elem[1] -= 1
    elif move == 'L':
        elem[0] -= 1
    else:
        elem[0] += 1

def distance(head, tail):
    '''
    Return distance between head and tail
    '''
    return (head[0] - tail[0])**2 + (head[1] - tail[1])**2

def part1(path):
    head = [0, 0]
    tail = [0, 0]

    positions = set()
    positions.add(tuple(tail))

    with open(path, 'r') as f:
        for line in f:
            move, count = line.split(' ')
            for _ in range(int(count)):
                update_position(head, move)

                #check distance between head and tail
                if distance(head, tail) >= 5:
                    second_move = None
                    if head[0] - tail[0] == 1:
                        second_move = 'R'
                    elif head[0] - tail[0] == -1:
                        second_move = 'L'
                    elif head[1] - tail[1] == 1:
                        second_move = 'U'
                    else:
                        second_move = 'D'

                    update_position(tail, move)
                    update_position(tail, second_move)
                elif distance(head, tail) > 2:
                    update_position(tail, move)

                #print(f'HEAD = {head} --- TAIL = {tail}')
                positions.add(tuple(tail))
            
    #print('Tail positions: ', positions)
    print('Answer Part 1: ', len(positions))

if __name__ == '__main__':
    #path to input file
    path = './code/day9/input.txt'

    part1(path)