import queue


def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return maze

def printMaze(maze, path=''):
    for i,v in enumerate(maze[0]):
        if v == 'O':
            start = i

    i = 0
    j= start
    pos = set()
    for move in path:
        if move == 'L':
            j -= 1
        elif move == 'R':
            j += 1
        elif move == 'U':
            i -= 1
        elif move == 'D':
            i += 1

        pos.add((i,j))

    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if (i, j) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    
    for i,v in enumerate(maze[0]):
        if v == 'O':
            start = i

    i = 0
    j= start
    for move in moves:
        if move == 'L':
            j -= 1
        elif move == 'R':
            j += 1
        elif move == 'U':
            i -= 1
        elif move == 'D':
            i += 1

        if not(0 <= i < len(maze) and 0 <= j < len(maze[0])):
                return False
        elif maze[i][j] == '#':
            return False
    return True

def findEnd(maze, moves):
    for i,v in enumerate(maze[0]):
        if v == 'O':
            start = i

    i = 0
    j= start
    for move in moves:
        if move == 'L':
            j -= 1
        elif move == 'R':
            j += 1
        elif move == 'U':
            i -= 1
        elif move == 'D':
            i += 1
        
    if maze[i][j] == 'X':
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False
        

if __name__ == "__main__":
    maze = createMaze2()
    # printMaze(maze, path='')
    q = queue.Queue()
    q.put('')
    path = ''

    while not findEnd(maze, path):
        path = q.get()
        for x in ['L', 'R', 'U', 'D']:
            put = path + x
            if valid(maze, put):
                q.put(put)