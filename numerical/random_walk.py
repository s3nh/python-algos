import random 


def random_walk(iter = 100, x_0 = 0.0, y_0 = 0.0, step_size = 1):
    _res = []
    for _iter in range(iter):
        _dice = random.random()
        if _dice < 0.5:
            x_0 += 1.0
        else:
            x_0 -= 1.0
        _res.append(x_0)

    return _res


def self_avoid_walk(width, height):

    visited = [[ False for col in range(width)] for row in range(height)]

    x = random.randint(0, width-1)
    y = random.randint(0, height -1)

    walk = [(x, y)]
    visited[x][y] = True

    while True:
        candidates = []
        candidates.append((x-1, y))
        candidates.append((x+1, y))
        candidates.append((x, y-1))
        candidates.append((x, y+1))

        neighbors = []
        for point in candidates:
            if (( point[0] >=0) and (point[0] < width) and 
                ( point[1] >=0) and (point[1] < height) and 
                not visited[point[0]][point[1]]):
                neighbors.append(point)

        if len(neighbors)==0:
            break

        # Random neighbor to visit 
        next = neighbors[random.randint(0, len(neighbors)-1)]
        walk.append(next)
        visited[next[0]][next[1]] = True
        x = next[0]
        y = next[1]

    return walk
