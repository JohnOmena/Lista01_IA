import copy
import sys
from puzzle import compare, valid, move, make_frontier, hashing


def dfs(max_level, board, p, current_level, l={}):
    global search, comparisons
    comparisons += 1
    x = hashing(board)
    if l.get(x, -1) != -1 or search == 1:
        return 0

    elif compare(board, p) == 0:
        print("DFS: ", comparisons)
        search = 1
        return 1

    elif current_level == max_level:
        return 0

    else:
        l[x] = 1
        frontier = make_frontier(board)
        current_level += 1

        for i in frontier:
            border = move(copy.deepcopy(board), i[0], i[1])
            dfs(max_level, border, p, current_level, l)

def dfs_depth_limited(board, max_level, p):
    global comparisons, search
    comparisons = search = 0
    sys.setrecursionlimit(1000000000)
    dfs(max_level, board, p, 0)
