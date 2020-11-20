class Node():
    def __init__(self, i=None, j=None, value=0, cost=float('inf'), heuristic=0, check=False, parent=None):
        self.i = i
        self.j = j
        self.value = value
        self.cost = cost
        self.heuristic = heuristic
        self.check = check
        self.parent = parent


matrix = [[Node() for j in range(30)] for i in range(30)]
with open('../Environment.txt', 'r') as f:
    i = 0
    for line in f:
        j = 0
        for num in line.split(","):
            w = matrix[i][j]
            if int(float(num)) == 1:
                w.value = 1
            w.j = j
            w.i = i
            j += 1
        i += 1

frontier = []


def up(i, j):
    try:
        if i > 0 and j > -1:
            x = matrix[i - 1][j]
            if x.value == 0:
                if not x.check and (i - 1, j) not in frontier:
                    frontier.append((i - 1, j))
                cost = (2 + matrix[i][j].cost)
                if x.cost > cost:
                    x.cost = cost
                    x.parent = matrix[i][j]
    except:
        pass


def down(i, j):
    try:
        if i > -1 and j > -1:
            x = matrix[i + 1][j]
            if x.value == 0:
                if not x.check and (i + 1, j) not in frontier:
                    frontier.append((i + 1, j))
                cost = (3 + matrix[i][j].cost)
                if x.cost > cost:
                    x.cost = cost
                    x.parent = matrix[i][j]
    except:
        pass


def left(i, j):
    try:
        if i > -1 and j > 0:
            x = matrix[i][j - 1]
            if x.value == 0:
                if not x.check and (i, j - 1) not in frontier:
                    frontier.append((i, j - 1))
                cost = (1 + matrix[i][j].cost)
                if x.cost > cost:
                    x.cost = cost
                    x.parent = matrix[i][j]
    except:
        pass


def right(i, j):
    try:
        if i > -1 and j > -1:
            x = matrix[i][j + 1]
            if x.value == 0:
                if not x.check and (i, j + 1) not in frontier:
                    frontier.append((i, j + 1))
                cost = (1 + matrix[i][j].cost)
                if x.cost > cost:
                    x.cost = cost
                    x.parent = matrix[i][j]
    except:
        pass


def add_frontier(i, j):
    up(i, j)
    down(i, j)
    left(i, j)
    right(i, j)
    # check_list[i][j] = 1
    matrix[i][j].check = True


def run(i, j, end_i, end_j):
    order = 0
    if matrix[i][j].value == 1:
        return False
    matrix[i][j].cost = 0
    while True:
        order += 1
        if matrix[i][j].check is False:
            add_frontier(i, j)
            if len(frontier) == 0:
                return False
            x = frontier[0]
            a = x[0]
            b = x[1]
            min = matrix[a][b].cost + matrix[a][b].heuristic

            for z in frontier:
                tmp = matrix[z[0]][z[1]].cost + matrix[z[0]][z[1]].heuristic
                if tmp < min:
                    min = tmp
                    a = z[0]
                    b = z[1]

            frontier.remove((a, b))
            i = a
            j = b

            if i == end_i and j == end_j:
                print('cost:', matrix[a][b].cost)
                print('order:', order)
                return True


def heuristic(i, j, end_i, end_j):
    x = i - end_i
    if x > 0:
        x = 2 * x
    else:
        x = 3 * x
    y = j - end_j
    result = abs(y) + abs(x)
    return result


def creat_heuristic_list(end_i, end_j):
    for i in range(30):
        for j in range(30):
            matrix[i][j].heuristic = heuristic(i, j, end_i, end_j)


def find_path(i, j, end_i, end_j):
    algorithm = input('chose your algorithm type A* or nothing (default is ucs): ')
    if algorithm == 'A*':
        creat_heuristic_list(end_i, end_j)
    if run(i, j, end_i, end_j):
        x = matrix[end_i][end_j]
        while x != None:
            print(x.i, x.j, end=' <- ')
            x = x.parent
    else:
        print('not find')


start_i = int(input('Enter start index start_i: '))
start_j = int(input('Enter start index start_j: '))
end_i = int(input('Enter start index end_i: '))
end_j = int(input('Enter start index end_j: '))
find_path(start_i, start_j, end_i, end_j)