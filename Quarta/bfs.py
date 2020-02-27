import copy
from puzzle import compare, move, make_frontier, hashing

def bfs(board, p):
    l = {}
    q = [board]
    comparisons = 0
    while q:
        v = q.pop(0)
        x = hashing(v)
        if l.get(x, -1) != -1:
            continue
        l[x] = 1

        if compare(v,p) == 0:
            print("Here: ",comparisons)
            return v
        else:
            frontier = make_frontier(v)
            for i in frontier:
                border = move(copy.deepcopy(v), i[0], i[1])
                q.append(border)
            comparisons += 1
    print("Hasn't been found")
